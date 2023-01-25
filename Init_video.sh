#!/bin/bash
ffmpeg -r 30 -f image2 -s 720x480 -i SampleImages/img_%04d.JPG -vcodec libx264 -crf 25  -pix_fmt yuv420p static/TimeLapse.mp4 -y