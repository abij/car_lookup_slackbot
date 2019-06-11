# Slack bot: Car Lookup

[![Build Status](https://dev.azure.com/alexanderbij/alexanderbij/_apis/build/status/abij.car_lookup_slackbot?branchName=master)](https://dev.azure.com/alexanderbij/alexanderbij/_build/latest?definitionId=1&branchName=master)

Slackbot to scan images for licence plates and report the known car details. The car owners are fetched from a csv-file on a fileshare.

![slack-bot-car-lookup](docs/slackbot-car-lookup.png)

## Hosting

- Create an app in [api.slack.com](https://api.slack.com/apps)
    - configure `/car` slack commmand
    - configure event-api on file_created / file_shared events in channel-scope
- Host as a docker container in the cloud, or use nGrok while testing.
    - Pass environment variables from Slack and/or opendata.rdw.nl
        - `ACTIVE_TOKEN` OAuth _Bot User OAuth Access Token_ (xoxb-***)
            - `CLIENT_ID` + `CLIENT_SECRET` and perform OAuth by '(Re)install app' in Slack API.
        - `RWD_APPTOKEN` (optional) the opendata.rdw.nl api-token

## Components:

- Open data: [RWD gekentekende voertuigen](https://opendata.rdw.nl/Voertuigen/Open-Data-RDW-Gekentekende_voertuigen/m9d7-ebf2)
- Github project: [Open Automated LicencePlate Recogniser](https://github.com/openalpr/openalpr)

## Testing locally

Only if Flask is running in debug mode:

- [http://localhost:5000/test?kenteken=28-ZTP-6](http://localhost:5000/test?kenteken=28-ZTP-6)
- [http://localhost:5000/test?file=someimage.jpg](http://localhost:5000/test?file=someimage.jpg)


#### TODO's:

- Make the bot Workspace independend: Its now for a single Workspace (Xebia) using one fileshare with a single csv-file.
- Make API calls in parallel to reduce total time for a request. (A slack command must answer in 3 sec.)
- Security: 
    - Limit the incoming traffic from Slack or validate event hashes. 
    - Add an TSL-certificate using letsencrypt
    - Pin Slack SSL certification.