# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Slack bot that handles Dutch license plate lookups via slash commands. Runs on Azure Functions (Consumption plan). Image scanning / ALPR has been removed.

## Commands

### Local development
```bash
# Install Azure Functions Core Tools (once)
brew install azure-functions-core-tools@4

# Copy and fill in settings
cp local.settings.json.example local.settings.json

# Install dependencies
pip install -r requirements.txt

# Run locally (listens on http://localhost:7071)
func start
```

Expose to Slack during local dev with `ngrok http 7071`, then set the slash command URL to `https://<ngrok-id>.ngrok.io/api/slack/commands`.

### Deploy to Azure (zip deploy, pre-built)
```bash
func azure functionapp publish <function-app-name> --build remote
```
`--build remote` bakes dependencies into the zip on Azure's build servers so they are not pip-installed at cold-start. Set `WEBSITE_RUN_FROM_PACKAGE=1` in the Function App's Application Settings so Azure mounts the zip directly without extracting it.

### Run tests
```bash
pip install pytest pytest-asyncio
pytest tests/ -v
pytest tests/test_image.py -v   # single file
```

### Lint
```bash
ruff format slackbot/ tests/
ruff check slackbot/ tests/
```

Linting config is in `pyproject.toml`: line length 120, Python 3.11 target.

## Architecture

### Request flow
```
Slack slash command POST
  → function_app.py  (HTTP trigger, signature verification)
  → bot.command_car()
  → asyncio.gather(owners.lookup, rdw.get_rdw_details, finnik.get_car_details)
  → messages.found_with_details()
  → plain-text response to Slack
```

### Key modules

| Module | Responsibility |
|--------|---------------|
| `function_app.py` | Azure Functions entry point; Slack signature verification; routes `/api/slack/commands` |
| `slackbot/bot.py` | `Bot` class; `command_car()` parses slash commands; `get_licence_plate_details()` runs concurrent lookups |
| `slackbot/rdw.py` | `RdwOnlineClient` — queries opendata.rdw.nl via Socrata/sodapy |
| `slackbot/finnik.py` | `FinnikOnlineClient` — scrapes finnik.nl for supplementary data (especially acceleration) |
| `slackbot/owners.py` | `CarOwners` — tag/untag/lookup owners; CSV backed by Azure Blob Storage (falls back to local file) |
| `slackbot/licence_plate.py` | Validates/normalizes against 14 Dutch plate patterns |
| `slackbot/messages.py` | Slack message templates and emoji formatting |

### Slash commands
- `/car <plate>` — look up a plate
- `/car tag <plate>` / `/car tag <plate> @user` / `/car tag <plate> "Name"` — register ownership
- `/car untag <plate>` — remove ownership


### Data sources
- **RDW** (authoritative): brand, model, catalogue price, APK expiry
- **Finnik** (supplementary): acceleration (0–100 km/h); RDW values take precedence when both return data
- **owners CSV**: persisted in Azure Blob Storage in production

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `SLACK_SIGNING_SECRET` | Yes | Slack app signing secret for request verification |
| `RWD_APPTOKEN` | No | Socrata app token for higher RDW rate limits |
| `AZURE_STORAGE_CONNECTION_STRING` | Prod | Blob Storage connection string for owners CSV |
| `AZURE_STORAGE_CONTAINER` | No | Blob container name (default: `slackbot`) |
| `AZURE_STORAGE_BLOB_NAME` | No | Blob file name (default: `car-owners.csv`) |
| `CAR_OWNERS_FILE` | No | Local CSV path used when no blob connection (default: `/tmp/car-owners.csv`) |

Copy `local.settings.json.example` → `local.settings.json` for local dev (not committed).

## Azure Setup Notes

- **Plan**: Consumption (free tier — 1M requests/month, 400K GB-s)
- **Storage account**: required by Azure Functions; also hosts the owners CSV blob
- **Python version**: 3.12 (last version supported on Linux Consumption plan)
- **Slack app config**: subscribe slash command `/car` to `https://<function-app>.azurewebsites.net/api/slack/commands`; no event subscriptions needed (image scanning removed)
