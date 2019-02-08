#!/usr/bin/env bash


# Compare the official version against an older version at my own repo!
# New version is based on Ubuntu 18 using new libs and failing on some images.

# DOCKER_IMAGE=${DOCKER_IMAGE:-"openalpr/openalpr"}
DOCKER_IMAGE=${DOCKER_IMAGE:-"bija/openalpr"}

docker run -it --rm \
    --volume $(pwd):/data:ro \
    --volume /dev/null:/dev/raw1394 \
    ${DOCKER_IMAGE} \
        --topn 3 \
        --country eu \
        --pattern nl \
        test_images/*