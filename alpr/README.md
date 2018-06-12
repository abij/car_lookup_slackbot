# Setup the ALPR in Docker

`docker pull openalpr/openalpr`

- Mount (-v) volume, the current directory $(pwd) as /data in the container.
- Mount /dev/null as /dev/raw1394 to prevent errors on the Mac. 
- The option `-c` is for Europe cars.

`docker run -it --rm -v $(pwd):/data:ro -v /dev/null:/dev/raw1394 openalpr/openalpr -c eu test_images/IMG_7725.JPG`