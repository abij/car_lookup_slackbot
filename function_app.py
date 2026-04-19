"""
Azure Functions entry point for the Car Lookup Slack bot.

Receives Slack slash command POSTs, verifies the request signature,
and delegates to the bot business logic.
"""
import hashlib
import hmac
import logging
import os
import time
import urllib.parse

import azure.functions as func

logging.getLogger("azure.core.pipeline.policies.http_logging_policy").setLevel(logging.WARNING)
from slackbot.bot import Bot

log = logging.getLogger(__name__)

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Single bot instance reused across warm invocations.
_bot: Bot | None = None


def _get_bot() -> Bot:
    global _bot
    if _bot is None:
        _bot = Bot()
    return _bot


def _verify_slack_request(req: func.HttpRequest, signing_secret: str) -> bool:
    timestamp = req.headers.get("X-Slack-Request-Timestamp", "")
    slack_signature = req.headers.get("X-Slack-Signature", "")

    if not timestamp or not slack_signature:
        return False

    try:
        if abs(time.time() - int(timestamp)) > 300:  # 5-minute replay window
            return False
    except ValueError:
        return False

    body = req.get_body().decode("utf-8")
    sig_basestring = f"v0:{timestamp}:{body}"
    computed = "v0=" + hmac.new(
        signing_secret.encode("utf-8"),
        sig_basestring.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(computed, slack_signature)


# TODO: Add a /api/slack/events endpoint for Slack Event Subscriptions.
#   - Event subscriptions are now disabled in the Slack app config
#   - Old URL was http://gdd-car-lookup-slackbot.westeurope.azurecontainer.io:5000/listening (ACI, gone)
#   - New URL will be https://car-lookup-fn.azurewebsites.net/api/slack/events
#   - Handle the url_verification challenge (one-time handshake)
#   - Listen for message.channels / message.groups events containing images
#   - Extract licence plates from images using AI (e.g. GPT-4o vision or Azure AI Vision)
#   - Look up each found plate and post the result back to the channel via the Slack Web API
#   - Requires SLACK_BOT_TOKEN env var and re-enabling Event Subscriptions + message events in the Slack app config

@app.route(route="slack/commands", methods=["POST"])
async def slack_commands(req: func.HttpRequest) -> func.HttpResponse:
    signing_secret = os.environ.get("SLACK_SIGNING_SECRET", "")
    if signing_secret and not _verify_slack_request(req, signing_secret):
        log.warning("Slack signature verification failed")
        return func.HttpResponse("Unauthorized", status_code=401)

    body = req.get_body().decode("utf-8")
    params = urllib.parse.parse_qs(body)

    command = params.get("command", [""])[0]
    text = params.get("text", [""])[0]
    user_id = params.get("user_id", [""])[0]

    log.info("Command %s from %s: %s", command, user_id, text)

    if command == "/car":
        result = await _get_bot().command_car(user_id, text)
        return func.HttpResponse(result, mimetype="text/plain")

    return func.HttpResponse("Unknown command", status_code=400)
