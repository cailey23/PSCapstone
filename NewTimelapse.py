import cv2
import os
import re

# set the path to the folder containing the images
path = '/Volumes/CaileyHP/CapstoneTimelapseSample/TestSample1'

# set the frame rate and resolution
fps = 30
resolution = (3840, 2160)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# a variable that numbers the output videos
j = 0

# a variable that sets the range of images to be processed
window = 200

# a variable that keeps track of which frames have been processed already
num_processed = 0

while True:
    # Get the list of all the image files in the folder
    images = [img for img in os.listdir(path) if img.endswith('.JPG')]

    # Sort the images in ascending order by file name
    images = sorted(images, key=lambda x: int(re.search(r'\d+', x).group()))
    to_process = images[num_processed: num_processed + window]
    if len (to_process) != window:
        continue

    output_file = 'output%s.mp4' % j
    # Create the video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, resolution)

    # Loop through each image and add it to the video writer object
    for i, image in enumerate (to_process):
        # Read the image file
        img = cv2.imread(os.path.join(path, image))

        # Resize the image to match the output resolution
        img = cv2.resize(img, resolution)

        # Write the image to the video
        out.write(img)
        print("fin", i )
        # Release the image from memory
        del img

    j += 1
    num_processed += window

    # Release the video writer object and close all windows
    out.release()


    #cv2.destroyAllWindows()
