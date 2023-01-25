""" make a time lapse
"""
from glob import glob
from typing import List

from cv2 import VideoWriter, imread, VideoWriter_fourcc, resize
import time

# to run shell scripts
import subprocess


class TimeLapse:
    def __init__(self, folder_path: str, width: int = 720, height: int = 480):
        self.folder_path = folder_path
        self.loaded_imgs = []
        self.fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
        self.width = width
        self.height = height

        self.vid_writer=None

    def get_filenames(self) -> List[str]:
        """
        retrieve the files from storage
        :param filepath: a glob to make files load
        :return: a sorted list of file names matching the filepath
        """
        files = glob(self.folder_path)
        files = sorted(files)
        print(f"Files retrieved: {len(files)}")
        return files

    def load_imgs(self, filenames):
        """ takes list of file names and loads them as images
        """
        for name in filenames:
            image = imread(name)
            image = resize(image, (self.width, self.height))
            self.loaded_imgs.append(image)

    def write_video(self) -> None:
        """
        load an image and write it to the video
        :param vid_writer:
        :param file_names:
        :return: nothing
        """
        for frame in self.loaded_imgs:
            self.vid_writer.write(frame)
        self.vid_writer.release()
        print(f"Wrote {len(self.loaded_imgs)} files")

    def initialize_video(self, current_files):
        self.vid_writer = VideoWriter("static/Timelapse.mp4", self.fourcc, 30, (self.width, self.height))
        self.load_imgs(current_files)
        self.write_video()

    def append_video(self, current_files):
        self.vid_writer = VideoWriter("static/Timelapse.mp4", self.fourcc, 30, (self.width, self.height))
        new_files = current_files[len(self.loaded_imgs):]
        self.load_imgs(new_files)
        self.write_video()

    def run(self):
        """
        Main function of this, using this right now so tests can be rune
        """
        while True:
            try:
                current_files = self.get_filenames()
                if not self.loaded_imgs:
                    self.initialize_video(current_files)
                    print("First time writing")
                elif len(current_files) > len(self.loaded_imgs):
                    self.append_video(current_files)
                    print("Wrote new files")
                else:
                    print("No new files")
                time.sleep(30)
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    time_lapse=TimeLapse("SampleImages")
    time_lapse.run()
