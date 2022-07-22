import os
from flask import Flask, request, make_response, render_template
from flask_ipban import IpBan
from slackeventsapi import SlackEventAdapter
import asyncio

from slackbot import bot

pyBot = bot.Bot()
app = Flask(__name__)
# https://github.com/Martlark/flask-ipban
ip_ban = IpBan(ban_count=10)
ip_ban.init_app(app)

# For (local) testing, I want to be able to start the app anyway.
if 'SLACK_SIGNING_SECRET' not in os.environ:
    # pylint: disable=E1101
    app.logger.error('Missing environment param: "SLACK_SIGNING_SECRET", cannot receive events from Slack!')
SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET', '')

slack_events_adapter = SlackEventAdapter(SIGNING_SECRET, "/listening", app)


# OAuth ########################################

@app.route("/install", methods=["GET"])
def pre_install():
    """This route renders the installation page with 'Add to Slack' button."""
    # Since we've set the client ID and scope on our Bot object, we can change
    # them more easily while we're developing our app.
    client_id = pyBot.oauth["client_id"]
    scope = pyBot.oauth["scope"]
    # Our template is using the Jinja templating language to dynamically pass
    # our client id and scope
    return render_template("install.html", client_id=client_id, scope=scope)


@app.route("/thanks", methods=["GET", "POST"])
def thanks():
    """
    This route is called by Slack after the user installs our app. It will
    exchange the temporary authorization code Slack sends for an OAuth token
    which we'll save on the bot object to use later.

    To let the user know what's happened it will also render a thank you page.
    """
    code_arg = request.args.get('code')
    # The bot's auth method to handles exchanging the code for an OAuth token
    pyBot.auth(code_arg)
    return render_template("thanks.html")


# Event api ########################################

@slack_events_adapter.on("file_created")
def event_file_created(event_data):
    team_id = event_data["team_id"]
    file_id = event_data["event"]["file_id"]
    # pylint: disable=E1101
    app.logger.info('Received "file_created" event, file_id: %s, team_id: %s', file_id, team_id)
    pyBot.lookup_car_from_file(team_id, file_id)


@slack_events_adapter.on("file_shared")
def event_shared_created(event_data):
    team_id = event_data["team_id"]
    file_id = event_data["event"]["file_id"]
    # pylint: disable=E1101
    app.logger.info('Received "file_shared" event, file_id: %s, team_id: %s', file_id, team_id)
    pyBot.lookup_car_from_file(team_id, file_id)


# Slack handles ########################################

@app.route("/kenteken", methods=["POST"])
@app.route("/my_car", methods=["POST"])
@app.route("/car", methods=["POST"])
def slack_commands():
    form_dict = request.form

    if not pyBot.is_valid_token(form_dict.get('token')):
        return make_response(401)  # unauthorized

    command = form_dict['command']
    text = form_dict['text']
    user_id = form_dict['user_id']  # Slack will render the Display name

    if command == '/car':
        return make_response(pyBot.command_car(user_id, text))

    if command in ['/my_car', '/kenteken']:
        return make_response("replaced with `/car`")

    # pylint: disable=E1101
    app.logger.warning('Incoming slack command is not implemented: %s', command)
    return make_response("Unknown command...")


@app.route("/test", methods=["GET"])
def testing():
    if not app.debug:
        return make_response("Only available when DEBUG is enabled", 405)

    params = request.args

    if 'file' in params.keys():
        file_path = os.path.join('/data', params.get('file'))
        result = list(pyBot.licenceplateExtractor.find_licenceplates(file_path))
    elif 'kenteken' in params.keys():
        # Python 3.6
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(pyBot.get_licence_plate_details(params.get('kenteken')))

        # Python 3.7+
        # result = asyncio.run(pyBot.get_licence_plate_details(params.get('kenteken')))
    else:
        return make_response('Usage examples: </br>'
                             '<a href="/test?file=IMG_3423.JPG">/test?file=IMG_3423.JPG</a></br>'
                             '<a href="/test?kenteken=12AB34">/test?kenteken=12AB34</a>')
    return make_response(str(result))


if __name__ == '__main__':
    is_debug_mode = os.environ.get('DEBUG', 'False').lower() in ['true', 'yes']
    app.run(debug=is_debug_mode, host='0.0.0.0')
