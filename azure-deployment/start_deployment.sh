#!/usr/bin/env bash

set -eu

rg="car-lookup-rg"

function execute_deployment()
{
    az group deployment create \
        --resource-group ${rg} \
        --name car_lookup_slack_api \
        --template-file azuredeploy.json \
        --parameters @az-deploy-params.json \
        --rollback-on-error \
        --output table

    az container attach -g ${rg} --name car-lookup-slackbot-api
}

function ask_correct_subscription()
{
    az account show -o table

    read -r -p "Is the correct subscription active to create resources? [y/N] " response
    case "$response" in
        [yY][eE][sS]|[yY])
            echo 'Oke, going to continue...'
            ;;
        *)
            echo 'First set the connect Azure subscription (az login / az account set <id>)'
            exit 1
            ;;
    esac
}

ask_correct_subscription
execute_deployment