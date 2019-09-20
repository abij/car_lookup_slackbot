import os
import tempfile
import requests
import logging
import hmac
import re

from threading import Lock

from slackclient import SlackClient
import tenacity

from slackbot.rdw import RdwOnlineClient
from slackbot.finnik import FinnikOnlineClient
from slackbot.owners import CarOwners
from slackbot.computervision import OpenAlprLicenceplaceExtractor
from slackbot import licence_plate
from slackbot import messages

log = logging.getLogger(__name__)

# To remember which teams have authorized your app and what tokens are
# associated with each team, we can store this information in memory on
# as a global object. When your bot is out of development, it's best to
# save this in a more persistent memory store.
authed_teams = {}

# Prevent duplicate lookups
# Especially when the Slack events 'file_created' and 'file_shared' are send both for the same file.
# Also prevent duplicate processing after retries, failures or timeouts.
seen_files = []

# We should check and add seen_files 1 thread at the time.
lock = Lock()


# Static functions.
def is_file_not_found(res):
    """
    :param res: dict: Slack API response
    :return: `True` when we should retry otherwise `False`
    """
    if not res['ok'] and 'file_not_found' in res['error']:
        log.info('Going to retry, because: "%s"', res['error'])
        return True
    return False


class Bot:
    """ Instantiates a Bot object to handle Slack events."""

    def __init__(self):
        super(Bot)
        self.name = "Car_info_bot"
        self.emoji = ":robot_face:"
        # When we instantiate a new bot object, we can access the app
        # credentials we set earlier in our local development environment.
        self.oauth = {"client_id": os.environ.get("CLIENT_ID"),
                      "client_secret": os.environ.get("CLIENT_SECRET"),
                      "scope": "bot"}
        self.verification = os.environ.get("VERIFICATION_TOKEN")

        # NOTE: Python-slack requires a client connection to generate
        # an oauth token. We can connect to the client without authenticating
        # by passing an empty string as a token and then reinstantiating the
        # client with a valid OAuth token once we have one.
        self.slack = SlackClient(os.environ.get("ACTIVE_TOKEN", ""))

        # Looking up the car-stat at the RDW.
        # The RWD_APPTOKEN is optional, but limits the amount of requests.
        self.rdw_client = RdwOnlineClient(os.environ.get('RWD_APPTOKEN'))

        # Keep track Kenteken -> SlackId + Name
        self.car_owners = CarOwners(csv_path=os.environ.get('CAR_OWNERS_FILE', '/data/car-owners.csv'))

        self.licenceplateExtractor = OpenAlprLicenceplaceExtractor()
        self.finnik_client = FinnikOnlineClient()

    def auth(self, code):
        """
        Authenticate with OAuth and assign correct scopes.
        Save a dictionary of authed team information in memory on the bot
        object.

        Parameters
        ----------
        code : str
            temporary authorization code sent by Slack to be exchanged for an
            OAuth token

        """
        # After the user has authorized this app for use in their Slack team,
        # Slack returns a temporary authorization code that we'll exchange for
        # an OAuth token using the oauth.access endpoint
        auth_response = self.slack.api_call(
            "oauth.access",
            client_id=self.oauth["client_id"],
            client_secret=self.oauth["client_secret"],
            code=code
        )
        # To keep track of authorized teams and their associated OAuth tokens,
        # we will save the team ID and bot tokens to the global
        # authed_teams object
        team_id = auth_response["team_id"]
        log.info('Authorized team_id: %s', team_id)
        authed_teams[team_id] = {"bot_token":
                                     auth_response["bot"]["bot_access_token"]}
        # Then we'll reconnect to the Slack Client with the correct team's
        # bot token

        token = authed_teams[team_id]["bot_token"]
        self.slack = SlackClient(token)

    def command_car(self, user_id, text):
        if 'help' in text.lower().strip() or len(text.lower().strip()) == 0:
            return messages.command_car_usage

        words = text.strip().split(" ")
        first_cmd = words[0]

        if len(words) == 1 and first_cmd.lower() in ['tag', 'untag']:
            return messages.command_tag_usage

        if len(words) == 1:
            plate = licence_plate.normalize(first_cmd)
            if not licence_plate.is_valid(plate):
                return messages.command_invalid_licence_plate(first_cmd)
            details = self.get_licence_plate_details(plate)
            if not details:
                return messages.lookup_no_details_found(plate)
            return messages.lookup_found_with_details(plate, details)

        sub_command = first_cmd.lower().strip()
        if sub_command in ['tag', 'untag']:
            plate = licence_plate.normalize(words[1])

            if not licence_plate.is_valid(plate):
                return messages.command_invalid_licence_plate(words[1])

            if 'tag' == sub_command:
                if len(words) == 2:
                    self.car_owners.tag(plate, slackid=user_id)
                    logging.info('Tagged "%s" to SlackId: %s  (executor: %s)', plate, user_id, user_id)
                    return messages.command_tag_added(plate, user_id=user_id)

                owner = str(' '.join(words[2:])).strip()
                match_in_quotes = re.match(r"[\"“](.+?)[\"”]", owner)

                owner_min_chars = 3
                owner_max_chars = 32

                if owner.startswith('@'):
                    owner_slack_id = owner
                    if owner_slack_id.lower() == '@me':
                        owner_slack_id = user_id
                    # TODO validate slackId with UserInfo

                    self.car_owners.tag(plate, slackid=owner_slack_id)
                    logging.info('Tagged "%s" to SlackId: %s  (executor: %s)', plate, owner_slack_id, user_id)
                    return messages.command_tag_added(plate, user_id=owner_slack_id)

                elif match_in_quotes:
                    owner = match_in_quotes.group(1)
                    if len(owner) < owner_min_chars or len(owner) > owner_max_chars or not self._is_valid_owner(owner):
                        return messages.command_invalid_owner(owner, min_chars=owner_min_chars,
                                                              max_chars=owner_max_chars)
                    self.car_owners.tag(plate, name=owner)
                    return messages.command_tag_added(plate, owner=owner)
                else:
                    return messages.command_invalid_owner(owner, min_chars=owner_min_chars, max_chars=owner_max_chars)

            if 'untag' == sub_command:
                self.car_owners.untag(user_id, plate)
                return messages.command_untag(plate)

        return messages.command_car_usage

    def lookup_car_from_file(self, team_id, file_id, threshold=80.0):
        if len(authed_teams) > 0 and team_id not in authed_teams:
            log.warning('Skipping: team_id %s is not in authorized list. (files.info): %s',
                        team_id, file_id)
        log.info('Going to fetch details (files.info) for file_id: %s...', file_id)

        # Wrapped in an inner function, so we can add a retry mechanism.
        # Sometimes the event that a new file is posted is received, but we cannot get the details yet.
        # We are too soon requesting the file info, I suppose.
        @tenacity.retry(
            stop=tenacity.stop_after_attempt(10),
            retry=(tenacity.retry_if_result(is_file_not_found)),
            wait=tenacity.wait_exponential(multiplier=1, min=2, max=10))
        def _inner(inner_file_id):
            return self.slack.api_call('files.info', file=inner_file_id)

        try:
            file_info_res = _inner(file_id)
        except tenacity.RetryError as e:
            log.warning('Skipping: Failed to fetch details (files.info): %s', e)
            return

        file_obj = file_info_res["file"]
        file_name = file_obj["name"]
        file_type = file_obj["pretty_type"]
        url_private_download = file_obj["url_private_download"]

        valid_file_types = ['png', 'jpg', 'jpeg']

        channel_ts_tuple = self._extract_ts_from_channel(file_obj)

        if not file_type.lower() in valid_file_types:
            log.info('Skipping: Not a valid file_type: %s (%s)', file_type, valid_file_types)
            return

        with lock:  # 1 thread at the time, prevent duplicate results
            if file_id in seen_files:
                log.info('Skipping: The file_id %s in list of seen_files, ignoring...', file_id)
                return
            else:
                seen_files.insert(0, file_id)  # insert in beginning,
                while len(seen_files) >= 50:  # prevent endless growing list.
                    seen_files.pop()  # remove at the end

        image_name = url_private_download.split('/')[-1]

        # Don't keep images, throw away when validated.
        with tempfile.NamedTemporaryFile(suffix=image_name, dir='/data/') as f:
            headers = {"Authorization": "Bearer " + self.slack.token}
            response = requests.get(url_private_download, headers=headers)

            f.write(response.content)
            f.flush()  # need to flush, else the file is 0 bytes...

            log.info('Downloaded (file_id) %s named: "%s" as tempfile "%s", trying to find licence plates...',
                     file_id, file_name, f.name)

            idx = -1  # marker for no results.
            for idx, match in enumerate(self.licenceplateExtractor.find_licenceplates(f.name)):
                confidence = match['confidence']
                plate = match['plate']
                valid = match['valid_nl_pattern']
                log.info('Found a licence place match: %s, confidence: %s, valid: %s', plate, confidence, valid)

                if confidence < threshold or not valid:
                    log.info('Valid pattern: %s or Confidence %s lower then threshold (%s).',
                             valid, confidence, threshold)
                    msg = messages.comment_found_but_skipping(plate, confidence, threshold, valid)
                    self.post_chat_message(channel_ts_tuple, file_id, msg, log_descr="Low confidence/Invalid pattern")
                    continue

                details = self.get_licence_plate_details(plate)
                if details:
                    msg = messages.comment_found_with_details(plate, confidence, details)
                else:
                    msg = messages.comment_found_no_details(plate, confidence)
                self.post_chat_message(channel_ts_tuple, file_id, msg, log_descr="car found")

            if idx == -1:
                self.post_chat_message(channel_ts_tuple, file_id, messages.comment_no_plate_found,
                                       log_descr="No plates found")

    def get_licence_plate_details(self, plate):
        result = {}

        plate = licence_plate.normalize(plate)
        # TODO: Async 3 services at the same time.
        try:
            owner_lookup = self.car_owners.lookup(plate)
            if owner_lookup:
                result.update({
                    'owner_slackid': owner_lookup['slackid'],
                    'owner_name': owner_lookup['name']})
        except Exception as e:
            log.warning('Failed to car_owner: %s', str(e))

        try:
            details = self.rdw_client.get_rdw_details(plate)
            if details:
                result.update(details)
        except Exception as e:
            log.warning('Failed to fetch RDW-details: %s', str(e))

        try:
            details = self.finnik_client.get_car_details(plate)
            if details:
                # Do not overwrite existing values.
                # So the RDW has preference over Finnik.
                missing_values = {k: v for k, v in details.items() if v and result.get(k) is None}
                result.update(missing_values)
        except Exception as e:
            log.warning('Failed to fetch acceleration from Finnik: %s', str(e))

        if len(result.keys()) == 0:
            return None
        return result

    def post_chat_message(self, channels_ts_tuples, file_id, msg, log_descr=None):
        # requires: chat:write:bot
        for idx, channels_ts_tuples in enumerate(channels_ts_tuples):
            channel, ts = channels_ts_tuples

            r = self.slack.api_call('chat.postMessage', channel=channel, thread_ts=ts, text=msg)
            result = 'success'
            if not r['ok']:
                result = r['error']
            log.info('Shared (%s/%s) channels): Posted message "%s" in channel_id: %s, about file_id: %s. Result: %s',
                     idx + 1, len(channels_ts_tuples), log_descr, channel, file_id, result)

    def is_valid_token(self, token):
        if self.verification:
            return hmac.compare_digest(self.verification, token)
        else:
            return True

    @staticmethod
    def _is_valid_owner(owner):
        return re.match(r"^[a-zA-Z]+(([',. -]{0,2}[a-zA-Z ])?[a-zA-Z.!?]*)*$", owner) is not None

    @staticmethod
    def _extract_ts_from_channel(json_input):
        channels = json_input["channels"]

        def extract_ts_for_channel(channel):
            shares = json_input["shares"]["public"][channel]

            # we're only interested in the message in #cars
            cars_share_ts = [share_info["ts"] for share_info in shares if share_info["channel_name"] == 'cars']

            if len(cars_share_ts) == 1:
                return channel, cars_share_ts[0]
            else:
                return channel, None

        return list(map(extract_ts_for_channel, channels))
