# Testing the OpenALPR on images

- Mount the current directory `$(pwd)` read-only as `/data` in the container.
- Mount `/dev/null` as `/dev/raw1394` to prevent errors on the Mac. 
- The option `-c` is for Europe cars.
- The option `-p` for Dutch pattern matching

**Using my version:**
`docker run -it --rm -v $(pwd):/data:ro -v /dev/null:/dev/raw1394 bija/openalpr -c eu -p nl test_images/politie1.JPG`

**Using the original:**
`docker run -it --rm -v $(pwd):/data:ro -v /dev/null:/dev/raw1394 openalpr/openalpr -c eu -p nl test_images/politie1.JPG`


> The original image _(openalpr/openalpr)_ has switched from Ubuntu 14 -> 18 and is having issues with OpenCV. 
Resulting on not recognizing plates in all images correclty.
