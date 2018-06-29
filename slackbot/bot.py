# -*- coding: utf-8 -*-
"""
Python Slack Bot class for use with the app
"""
import os
import subprocess
import tempfile
import requests
import re
import psycopg2
from psycopg2.extras import RealDictCursor


from slackclient import SlackClient

# To remember which teams have authorized your app and what tokens are
# associated with each team, we can store this information in memory on
# as a global object. When your bot is out of development, it's best to
# save this in a more persistent memory store.
authed_teams = {}

# To prevent duplicate lookups (retries):
seen_files = []

LOOKUP_QUERY = '''
select *
from voertuigen v
left join carowners c on c.kenteken = v.kenteken
where v.kenteken = %s;
'''

COMMENT_WITH_DETAILS = '''
:mega: Found licence plate *{plate}* _(confidence {confidence})_!
It's a *{car_type}* of brand *{car_brand}*
> • Owner: {owner}
> • Price: {price} 
> • APK expires: {apk}'''

COMMENT_NO_DETAILS = 'I found *{plate}* _(confidence {confidence})_, but no extra info associated with it...'


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
                      # Scopes provide and limit permissions to what our app
                      # can access. It's important to use the most restricted
                      # scope that your app will need.
                      "scope": "bot"}
        self.verification = os.environ.get("VERIFICATION_TOKEN")

        # Optionally provide the known token:
        token = os.environ.get("ACTIVE_TOKEN", "")

        # NOTE: Python-slack requires a client connection to generate
        # an oauth token. We can connect to the client without authenticating
        # by passing an empty string as a token and then reinstantiating the
        # client with a valid OAuth token once we have one.
        self.client = SlackClient(token)

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
        auth_response = self.client.api_call(
                                "oauth.access",
                                client_id=self.oauth["client_id"],
                                client_secret=self.oauth["client_secret"],
                                code=code
                                )
        # To keep track of authorized teams and their associated OAuth tokens,
        # we will save the team ID and bot tokens to the global
        # authed_teams object
        team_id = auth_response["team_id"]
        authed_teams[team_id] = {"bot_token":
                                 auth_response["bot"]["bot_access_token"]}
        # Then we'll reconnect to the Slack Client with the correct team's
        # bot token
        token = authed_teams[team_id]["bot_token"]
        self.client = SlackClient(token)
        print('OAuth complete: ' + token)

    def lookup_car(self, file_id):
        file_info_res = self.client.api_call('files.info', file=file_id)
        if not file_info_res['ok']:
            print('Failed response: ' + file_info_res['error'])
            return

        file_obj = file_info_res["file"]
        file_type = file_obj["pretty_type"]
        url_private_download = file_obj["url_private_download"]

        if not file_type.lower() in ['png', 'jpg', 'jpeg']:
            return  # Not an image we can parse
        if file_id in seen_files:
            return  # No need to lookup this file, seen it already.

        image_name = url_private_download.split('/')[-1]

        # Don't keep images, throw away when validated.
        with tempfile.NamedTemporaryFile(suffix=image_name,
                                         dir='/data/') as f:
            seen_files.insert(0, file_id)
            while len(seen_files) >= 50:  # prevent endless growing list.
                seen_files.remove(len(seen_files) - 1)

            headers = {"Authorization": "Bearer " + self.client.token}
            response = requests.get(url_private_download, headers=headers)

            f.write(response.content)
            f.flush()  # need to flush, else the file is 0 bytes...

            res = self.alpr_best_match(f.name)

            if res and float(res['confidence']) > 88.0:
                details = self.get_details(res['plate'])
                return self.comment_on_image(file_id,
                                             res['plate'],
                                             res['confidence'],
                                             details)
            else:
                print('Image lookup result: ' + str(res))

    def comment_on_image(self, file_id, plate, confidence, details):
        if details:
            msg = COMMENT_WITH_DETAILS.format(
                plate=plate,
                confidence=confidence,
                car_type=details.get('handelsbenaming') or '-',
                car_brand=details.get('merk') or '-',
                owner=details.get('owner') or '-',
                apk=details.get('dt_verval_apk') or '-',
                price=details.get('catalogusprijs') or '-')
        else:
            msg = COMMENT_NO_DETAILS.format(plate=plate, confidence=confidence)

        self.client.api_call('files.comments.add',
                             file=file_id,
                             comment=msg)

    @staticmethod
    def alpr_best_match(file_name):
        """
        Take the first match with highest confidence.

        :param file_name: File to check
        :return: {'conf': '95.0374', 'plate': 'ND5222'} or None
        """
        file_path = '/data/' + file_name
        stdout = subprocess.getoutput('alpr ' + file_path)
        output = [line.strip(' -') for line in stdout.splitlines()]
        summary = output[0]

        if not re.match('plate0: \d+ results', summary):
            if 'No license plates found' in summary:
                return
            elif 'Image file not found' in summary:
                print('ERROR: Incorrect config! Cannot find ' + file_path)
                return
            else:
                print('ERROR: ' + summary)
                return

        best_match = output[1]  # example: ND11XX\t confidence: 95.0374

        pattern = '(?P<plate>.+)\t +confidence: (?P<confidence>\d+.\d+)'
        matched = re.match(pattern, best_match)
        if matched:
            return matched.groupdict()

    @staticmethod
    def get_details(kenteken):
        #TODO: implement a lookup in Files on the blob, which is very cheap & slow
        #TODO: use secrets pass them around
        with psycopg2.connect(host='host.docker.internal',
                              dbname='postgres',
                              user='postgres',
                              password='example',
                              cursor_factory=RealDictCursor) as conn:
            with conn.cursor() as curs:
                curs.execute(LOOKUP_QUERY, (kenteken,))
                return curs.fetchone()
