""" make a time lapse
"""
from glob import glob
from cv2 import VideoWriter, imread, VideoWriter_fourcc, resize
import time

#to run shell scripts
import subprocess

def get_filenames (filepath: str) -> list:
    """
    retrieve the files from storage
    :param filepath: a glob to make files load
    :return: a sorted list of file names matching the filepath
    """
    files = glob (filepath)
    files = sorted (files)
    print(f"Files retrieved: {len(files)}")
    return files


def load_imgs (filenames: list, imgs: list, width: int, height: int):
    """ takes list of file names and loads them as images
    """
    for name in filenames:
        image = imread (name)
        image = resize (image, (width, height))
        imgs.append(image)
    return imgs


def write_video (vid_writer: VideoWriter, imgs: list) -> None:
    """
    load an image and write it to the video
    :param vid_writer:
    :param file_names:
    :return: nothing
    """
    for frame in imgs:
        vid_writer.write (frame)
    video_obj.release()
    print (f"Wrote {len(imgs)} files")


folder_path = "/Volumes/CaileyHP/Capstone timelapse sample/Test sample 2/*.JPG"
files_read = []
loaded_imgs = []
fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
width, height = 720, 480


while True:
    try:
        current_files = get_filenames(folder_path)
        if files_read == []:
            video_obj = VideoWriter("static/Timelapse.mp4", fourcc, 30, (width, height))
            loaded_imgs = load_imgs(current_files, loaded_imgs, width, height)
            write_video (video_obj, loaded_imgs)
            files_read = current_files
            print("First time writing")

        if len(current_files) > len(files_read):
            video_obj = VideoWriter("static/Timelapse.mp4", fourcc, 30, (width, height))
            new_files = current_files[len(files_read):]
            loaded_imgs = load_imgs (new_files, loaded_imgs, width, height)
            write_video(video_obj, loaded_imgs)
            files_read = files_read + new_files
            print ("Wrote new files")
        else:
            print ("No new files")

        if len(current_files) == len(files_read):
            time.sleep(30)

    except KeyboardInterrupt:
        break

#files = get_files("/Volumes/CaileyHP/RIT/Junior/Fall 2020/Scientific Photography/Asgmt5.TimeLapse/*.JPG")
