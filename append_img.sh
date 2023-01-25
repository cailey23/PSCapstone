#!/bin/bash
ffmpeg -r 30 -f image2 -s 720x480 -start_number 0 -i SampleImages/img_%04d.JPG -vcodec libx264 -crf 25  -pix_fmt yuv420p temp.mp4 -y
ffmpeg -f concat -i videos.txt -c copy static/TimeLapse.mp4 -y