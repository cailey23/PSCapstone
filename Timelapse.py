from typing import Tuple

import cv2
import os
import re

from capture_images import start_capture
from stichvideo import stitch_video


def TimeLapse (fps: int = 30, resolution: Tuple[int, int] = (3840, 2160), frequency_s: int = 10,
               num_images_to_capture: int = 30):
    # set the path to the folder containing the images
    path = '/Volumes/CaileyHP/CapstoneTimelapseSample/TestSample1'

    # set the frame rate and resolution
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # a variable that numbers the output videos
    j = 0

    # a variable that sets the range of images to be processed
    window = 200

    # a variable that keeps track of which frames have been processed already
    num_processed = 0

    get_images, is_finished = start_capture(frequency_s=frequency_s, num_images=num_images_to_capture, image_folder=path)
    videos=[]

    while not is_finished():
        # get the list of all the image files in the folder
        images = get_images(num_processed)#[img for img in os.listdir(path) if img.endswith('.JPG')]

        # sort the images in ascending order by file name
        # images = sorted(images, key=lambda x: int(re.search(r'\d+', x).group()))
        # to_process = images[num_processed: num_processed + window]
        if len (images) != window:
            continue

        output_file = 'output%s.mp4' % j
        videos.append(output_file)
        # create the video writer object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, fps, resolution)

        # loop through each image and add it to the video writer object
        for i, image in enumerate (images):
            # read the image file
            img = cv2.imread(os.path.join(path, image))

            # resize the image to match the output resolution
            img = cv2.resize(img, resolution)

            # write the image to the video
            out.write(img)
            print("fin", i )
            # release the image from memory
            del img

        j += 1
        num_processed += window

        # Release the video writer object and close all windows
        out.release()
        stitch_video(video_files=videos, video_output_folder="static")


        #cv2.destroyAllWindows()
