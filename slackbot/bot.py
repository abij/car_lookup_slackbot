# -*- coding: utf-8 -*-
"""
Python Slack Bot class for use with the app
"""
import os
import tempfile
import requests

from slackclient import SlackClient

# To remember which teams have authorized your app and what tokens are
# associated with each team, we can store this information in memory on
# as a global object. When your bot is out of development, it's best to
# save this in a more persistent memory store.
authed_teams = {}


car_with_owner = """
Found {{ merk }} - {{ handelsbenaming }} based on {{ kenteken }}. It's **{{ owner }}**. 
Fun facts: 
 - APK will expire at {{ dt_verval_apk }} 
 - Catalogus price {{ catalogusprijs }}
"""

car_no_owner = """
Found {{ merk }} - {{ handelsbenaming }} based on {{ kenteken }}. Unknown owner.
Fun facts: 
 - APK will expire at {{ dt_verval_apk }} 
 - Catalogus price {{ catalogusprijs }}
"""
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

        if not file_type.lower() in ['png', 'jpeg']:
            return

        with tempfile.TemporaryFile() as fp:
            headers = {"Authorization": "Bearer " + self.client.token}
            img_response = requests.get(url_private_download, headers=headers)
            fp.write(img_response.content)
            print('I have downded the file')
            # #TODO go though ANPT
            # if found_car:
            #     self.client.api_call('files.comments.add',
            #                      file=file_id,
            #                      comment='Found a ')
