#!/usr/bin/env bash

set -xue

# My own docker-hub:
docker build . -t bija/car_lookup

docker run \
    --cpus=1 \
    --memory=1G \
    -e DEBUG=${DEBUG:-"True"} \
    -e ACTIVE_TOKEN=${SLACK_ACTIVATION_TOKEN:-""} \
    -e RWD_APPTOKEN=${RDW_APPTOKEN:-""} \
    -v /dev/null:/dev/raw1394 \
    -v /Users/alexanderbij/dev/gdd/car_lookups/alpr/test_images:/data \
    -p 5000:5000 bija/car_lookup:latest