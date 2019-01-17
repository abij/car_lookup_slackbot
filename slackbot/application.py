import os
from flask import Flask, request, make_response, render_template

from slackbot import bot

pyBot = bot.Bot()
app = Flask(__name__)


def _event_handler(event_type, slack_event):
    """
    A helper function that routes events from Slack to our Bot
    by event type and subtype.
    """
    team_id = slack_event["team_id"]

    # ================ File created Events =============== #
    # A file is uploaded!
    if event_type == "file_created":
        file_id = slack_event["event"]["file_id"]
        app.logger.info('Received "file_created" event, file_id: %s', file_id)
        pyBot.lookup_car_from_file(team_id, file_id)
        return make_response("File message received", 200,)

    # ============= Event Type Not Found! ============= #
    message = "You have not added an event handler for the %s" % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


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


@app.route("/listening", methods=["GET", "POST"])
def hears():
    """
    This route listens for incoming events from Slack and uses the event
    handler helper function to route events to our Bot.
    """
    slack_event = request.get_json()

    # ============= Slack URL Verification ============ #
    # In order to verify the url of our endpoint, Slack will send a challenge
    # token in a request and check for this token in the response our endpoint
    # sends back.
    #       For more info: https://api.slack.com/events/url_verification
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200,
                             {"content_type": "application/json"})

    # ============ Slack Token Verification =========== #
    # We can verify the request is coming from Slack by checking that the
    # verification token in the request matches our app's settings
    if pyBot.verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s \npyBot has: \
                   %s\n\n" % (slack_event["token"], pyBot.verification)
        # By adding "X-Slack-No-Retry" : 1 to our response headers, we turn off
        # Slack's automatic retries during development.
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    # ====== Process Incoming Events from Slack ======= #
    # If the incoming request is an Event we've subcribed to
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        # Then handle the event by event_type and have your bot respond
        return _event_handler(event_type, slack_event)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})


@app.route("/kenteken", methods=["POST"])
@app.route("/my_car", methods=["POST"])
def slack_commands():
    form_dict = request.form

    command = form_dict['command']
    user_id = form_dict['user_id']  # Slack will render the Display name
    text = form_dict['text']

    if command == '/my_car':
        return make_response(pyBot.command_my_car(user_id, text))

    if command == '/kenteken':
        return make_response(pyBot.command_kenteken(text))

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
        result = pyBot.get_kenteken_details(params.get('kenteken'))
    else:
        return make_response('Usage examples: </br>'
                             '<a href="/test?file=IMG_3423.JPG">/test?file=IMG_3423.JPG</a></br>'
                             '<a href="/test?kenteken=12AB34">/test?kenteken=12AB34</a>')
    return make_response(str(result))


if __name__ == '__main__':
    is_debug_mode = os.environ.get('DEBUG', 'False').lower() in ['true', 'yes']
    app.run(debug=is_debug_mode, host='0.0.0.0')
