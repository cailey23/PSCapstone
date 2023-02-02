"""
Has a thread for capturing images
"""
import time
from glob import glob

import gphoto2 as gp
import threading


class CaptureImageThread(threading.Thread):
    def __init__(self, image_template: str, duration_s: int, frequency_s: int, image_files: list):
        super().__init__()
        self.image_files = image_files
        self.image_template = image_template
        self.frequency_s = frequency_s
        self.duration_s = duration_s

        self.daemon = True  # This sets the thread to end when the main program ends

    def run(self):
        camera = gp.Camera()
        start_time = time.time()
        most_recent_capture_time = 0
        count = 0
        while time.time() < start_time + self.duration_s:
            try:
                if most_recent_capture_time < time.time() + self.frequency_s:
                    path = camera.capture(gp.GP_CAPTURE_IMAGE)
                    most_recent_capture_time = time.time()
                    camera_file = camera.file_get(path.folder, path.name, gp.GP_FILE_TYPE_NORMAL)
                    camera_file.save(self.image_template % count)
                    camera.file_delete(path.folder, path.name)
                    self.image_files.append(self.image_template % count)
                    count += 1
            except:
                print("The Camera is disconnected")  # This will just spam print if the camera is disconnected
                camera = gp.Camera()


class AbstractCamera(threading.Thread):
    def __init__(self, image_folder: str, image_files: list):
        super().__init__()
        self.image_files = image_files
        self.image_folder = image_folder

        self.daemon = True  # This sets the thread to end when the main program ends

    def run(self):
        """
        copied from TimeLapse's get_filenames
        """
        while True:
            files = glob(self.image_folder)
            files = sorted(files)
            print(f"Files retrieved: {len(files)}")
            self.image_files.clear()
            self.image_files.extend(files)
            time.sleep(10)


def main():
    image_files = []
    capture_image = CaptureImageThread('SampleImages/frame%04d.jpg', 20, 2, image_files)
    capture_image.start()
    time.sleep(4)
    print(image_files)
    capture_image.join()
    print(image_files)


if __name__ == "__main__":
    main()
