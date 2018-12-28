# Slack Car bot

## Components:
- Open data: [RWD gekentekende voertuigen](https://opendata.rdw.nl/Voertuigen/Open-Data-RDW-Gekentekende_voertuigen/m9d7-ebf2) (~7Gb)
- Github project: [Open Automated LicencePlate Recogniser](https://github.com/openalpr/openalpr)


> Latest version is using RDW online, not a offline database dump.

    $ # Loading data is optional:
    $ docker run --name postgres -e POSTGRES_PASSWORD=example -d postgres
    $ data/load_data.sh
    
    $ docker build -t bija/car_lookup .
    $ docker run -e ACTIVE_TOKEN=xyz -v /dev/null:/dev/raw1394 -p 5000:5000 bija/car_lookup


## Testing locally 

Passthrough port 5000 from a public internet address.
https://dashboard.ngrok.com/get-started

https://godatadriven.slack.com/apps/manage


## Deploying



### TODO:
 
 