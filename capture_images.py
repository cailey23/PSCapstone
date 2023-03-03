"""
Has a thread for capturing images
"""
import time
from datetime import date
from glob import glob

import gphoto2 as gp
import threading


def reconnect():
    is_connected = False
    while not is_connected:
        try:
            return gp.Camera()
        except gp.GPhoto2Error as e:
            if "[-105]" not in str(e):
                raise e


class CaptureImageThread(threading.Thread):
    def __init__(self, image_folder: str, num_images: int, frequency_s: int, image_files: list):
        super().__init__()
        self.image_files = image_files
        self.image_folder = image_folder
        self.frequency_s = frequency_s
        self.num_images = num_images

        self.daemon = True  # This sets the thread to end when the main program ends

    def run(self):
        camera = gp.Camera()
        most_recent_capture_time = 0
        count = 0
        while len(self.image_files) < self.num_images:
            try:
                if most_recent_capture_time < time.time() + self.frequency_s:
                    path = camera.capture(gp.GP_CAPTURE_IMAGE)
                    most_recent_capture_time = time.time()
                    camera_file = camera.file_get(path.folder, path.name, gp.GP_FILE_TYPE_NORMAL)
                    image_file = self.image_folder + f"/Image_{time.strftime('%Y_%m_%d_%S')}.jpg"
                    camera_file.save(image_file)
                    camera.file_delete(path.folder, path.name)
                    self.image_files.append(image_file)
                    count += 1
            except gp.GPhoto2Error as e:
                print("Camera is disconnected")
                camera = reconnect()



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
            self.image_files.clear()
            self.image_files.extend(files)
            time.sleep(10)


def get_new_images(image_files, num_images_obtained):
    return image_files[num_images_obtained:]


def check_finshed(capture_image_thread):
    return not capture_image_thread.is_alive()


def start_capture(frequency_s: int, num_images: int, image_folder: str):
    """
    Starts a capture of the image
    @param frequency_s: Wait time between images in seconds
    @param num_images: Number of images to be taken
    @param image_folder: The folder where the images get saved to
    @returns get_images: function that gets new images with the parameter of the number of images already obtained
    @returns is_finished: function that checks whether the code is still capturing
    """
    image_files = []
    image_capture = CaptureImageThread(image_folder, num_images, frequency_s, image_files)
    image_capture.start()

    return lambda num_image_obtained: get_new_images(image_files, num_image_obtained), lambda: check_finshed(
        image_capture)


def start_abstract_capture(image_folder):
    """
    treats a folder as if it were a camera and updates the new images every 10 seconds
    @param image_folder: the folder with images
    @returns get_images: function that
    """
    image_files = []
    image_capture = AbstractCamera(image_folder, image_files)
    image_capture.start()

    return lambda num_image_obtained: get_new_images(image_files, num_image_obtained)


if __name__ == "__main__":
    """
    This is an example of calling this 
    Real image capture: 
    """
    # Real image capturing: capturing images every 3 seconds for a total of 5 images
    get_images, is_finished = start_capture(3, 5, "SampleImageLocation")
    while not is_finished():
        print(get_images(0))
        time.sleep(5)
    print(get_images(0))
    print(get_images(3))

    # Treating folder as capturing
    get_images = start_abstract_capture("SampleImageLocation/*.jpg")
    time.sleep(1)
    print(get_images(0))