# -*- coding: utf-8 -*-
"""
Python Slack Bot class for use with the app
"""
import os
import tempfile
import requests
import re
import logging

from slackclient import SlackClient
from retrying import retry

from rdw import RdwOnlineClient
from owners import CarOwners
import computervision

log = logging.getLogger()

# To remember which teams have authorized your app and what tokens are
# associated with each team, we can store this information in memory on
# as a global object. When your bot is out of development, it's best to
# save this in a more persistent memory store.
authed_teams = {}

# To prevent duplicate lookups (retries):
seen_files = []

KENTEKEN_DETAILS_MSG = '''
Lookup of {kenteken}: *{car_type}* of brand *{car_brand}*
> • Owner: {owner}
> • Price: {price} 
> • APK expires: {apk}'''

COMMENT_WITH_DETAILS = '''
:mega: Found licence plate *{plate}* _(confidence {confidence:.2f})_!
It's a *{car_type}* of brand *{car_brand}*
> • Owner: {owner}
> • Price: {price} 
> • APK expires: {apk}'''

COMMENT_NO_DETAILS = 'I found *{plate}* _(confidence {confidence:.2f})_, but no extra info associated with it...'


# Static functions.
def retry_on_file_not_found(result):
    if 'ok' not in result and 'file_not_found' in result['error']:
        log.info('Retry to fetch file_id details, because "file_not_found"...')
        return True
    return False


def get_owner_from_details(details, default="-"):
    result = default
    if details.get('owner_slackid') is not None:
        result = '<@{}>'.format(details.get('owner_slackid'))
    elif details.get('owner_name') is not None:
        result = details.get('owner_name')
    return result


class Bot(object):
    """ Instantiates a Bot object to handle Slack events."""
    def __init__(self):
        super(Bot, self).__init__()
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

        #key = os.environ.get('AZ_COGNITIVE_SERVICES_KEY', '')
        #self.licenceplateExtractor = computervision.AzureCongitiveOCRLicenceplaceExtractor(key)
        self.licenceplateExtractor = computervision.OpenAlprLicenceplaceExtractor()

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

    def command_kenteken(self, text):
        usage = 'Lookup car details including the owner (if known):\n' \
                '`AA-12-BB`  _(dashes are optional)_'

        if 'help' in text.lower().strip():
            return usage

        kenteken = text.replace('-', '').upper()
        if not re.match('\w+-?\w+-?\w+', kenteken) or len(kenteken) != 6:
            return 'Input ({}) does not look like a valid licence plate'.format(text)

        details = self.get_kenteken_details(kenteken)
        if not details:
            return 'No details found...'

        return KENTEKEN_DETAILS_MSG.format(
            kenteken=text,
            car_type=details.get('handelsbenaming') or '-',
            car_brand=details.get('merk') or '-',
            owner=get_owner_from_details(details),
            apk=details.get('vervaldatum_apk') or '-',
            price=details.get('catalogusprijs') or '-')

    def command_my_car(self, user_id, text):
        usage = 'Register or unregister a car to your Slack handle:\n' \
                ' `tag AA-12-BB`  _(to add a car that belongs to you)_\n' \
                ' `untag AA-12-BB`  _(removes this car)_'

        if 'help' in text.lower().strip():
            return usage

        words = text.split(" ")
        subcommand = words[0]

        if len(words) != 2:
            return 'Invalid nr of arguments. Expects 2, given {}.\nUsage:\n{}'.format(len(words), usage)

        kenteken = words[1]
        kenteken = kenteken.replace('-', '').upper()

        if len(kenteken) != 6:
            return 'Invalid kenteken, should be 8 chars (including minus signs)'

        if 'tag' in subcommand.lower():
            # TODO lookup the real name of the user, for the csv.
            self.car_owners.tag(user_id, kenteken, name="")
            return 'Added {} to your slack handle'.format(kenteken)
        elif 'untag' in subcommand.lower():
            self.car_owners.untag(user_id, kenteken)
            return 'Removed the liceneplate {}'.format(kenteken)

        return usage

    @retry(stop_max_attempt_number=10,
           wait_exponential_multiplier=1000,
           wait_exponential_max=5000,
           retry_on_result=retry_on_file_not_found)
    def get_file_info(self, file_id):
        return self.slack.api_call('files.info', file=file_id)

    def lookup_car_from_file(self, team_id, file_id, threshold=60.0):
        log.info('Going to process file with id: %s...', file_id)
        file_info_res = self.get_file_info(file_id)
        if not file_info_res['ok']:
            log.warning('Failed response (files.info): %s', file_info_res['error'])
            return

        file_obj = file_info_res["file"]
        file_type = file_obj["pretty_type"]
        channels = file_obj["channels"]
        url_private_download = file_obj["url_private_download"]

        if not file_type.lower() in ['png', 'jpg', 'jpeg']:
            log.info('Not a valid file_type: ' + file_type)
            return
        if file_id in seen_files:
            log.info('File_id %s in list of seen_files, ignoring...', file_id)
            return

        image_name = url_private_download.split('/')[-1]

        # Don't keep images, throw away when validated.
        with tempfile.NamedTemporaryFile(suffix=image_name, dir='/data/') as f:

            seen_files.insert(0, file_id)
            while len(seen_files) >= 50:  # prevent endless growing list.
                seen_files.remove(len(seen_files) - 1)

            headers = {"Authorization": "Bearer " + self.slack.token}
            response = requests.get(url_private_download, headers=headers)

            f.write(response.content)
            f.flush()  # need to flush, else the file is 0 bytes...

            #TODO Based on the
            match = self.licenceplateExtractor.find_licenceplates(f.name)
            if match is None:
                return

            confidence = match['confidence']
            kenteken = match['plate']
            log.info('Found a licenplace match: %s confidence: %s', kenteken, confidence)

            if confidence < threshold:
                log.info('Confidence %s, lower then threshold (%s), not commenting on image...', confidence, threshold)
                return

            details = self.get_kenteken_details(kenteken)
            self.comment_on_image(channels, file_id, kenteken, confidence, details)

    def comment_on_image(self, channels, file_id, plate, confidence, details):
        if details:
            msg = COMMENT_WITH_DETAILS.format(
                plate=plate,
                confidence=confidence,
                car_type=details.get('handelsbenaming') or '-',
                car_brand=details.get('merk') or '-',
                owner=get_owner_from_details(details),
                apk=details.get('vervaldatum_apk') or '-',
                price=details.get('catalogusprijs') or '-')
        else:
            msg = COMMENT_NO_DETAILS.format(plate=plate, confidence=confidence)

        # Comments have changed: https://api.slack.com/changelog/2018-05-file-threads-soon-tread
        # So lets post a message instead of commenting on the file...
        # requires: chat:write:bot

        for idx, channel_id in enumerate(channels):
            r = self.slack.api_call('chat.postMessage', channel=channel_id, text=msg)

            result = 'success'
            if not r['ok']:
                result = r['error']

            log.info('Shared (%s/%s) channels): Posted message in channel_id: %s, about file_id: %s. Result: %s',
                     idx+1, len(channels), channel_id, file_id, result)

    def get_kenteken_details(self, kenteken):
        result = {}

        kenteken = kenteken.strip().replace('-', '').upper()

        try:
            owner_lookup = self.car_owners.lookup(kenteken)
            if owner_lookup:
                result.update({
                    'owner_slackid': owner_lookup['slackid'],
                    'owner_name': owner_lookup['name']})
        except Exception as e:
            log.warning('Failed to car_owner: %s', str(e))

        try:
            details = self.rdw_client.get_rdw_details(kenteken)
            if details:
                result.update(details)
        except Exception as e:
            log.warning('Failed to fetch RDW-details: %s', str(e))

        if len(result.keys()) == 0:
            return None
        return result
