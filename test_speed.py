import unittest
from cv2 import VideoWriter, imread, VideoWriter_fourcc, resize

from TimeLapse import get_filenames, write_video, load_imgs

class SpeedTest(unittest.TestCase):
    def test_initialize_no_images(self):
        files_read = []
        loaded_imgs = []
        fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
        width, height = 720, 480

        current_files = []
        video_obj = VideoWriter("static/Timelapse.mp4", fourcc, 30, (width, height))
        loaded_imgs = load_imgs(current_files, loaded_imgs, width, height)
        write_video (video_obj, loaded_imgs)
        files_read = current_files

    def test_initialize_one_image(self):
        files_read = []
        loaded_imgs = []
        fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
        width, height = 720, 480

        current_files = ["SampleImages/img1.JPG"]
        video_obj = VideoWriter("static/Timelapse.mp4", fourcc, 30, (width, height))
        loaded_imgs = load_imgs(current_files, loaded_imgs, width, height)
        write_video(video_obj, loaded_imgs)
        files_read = current_files

    def test_initialize_100_image(self):
        files_read = []
        loaded_imgs = []
        fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
        width, height = 720, 480

        current_files = ["SampleImages/img1.JPG"]*100
        video_obj = VideoWriter("static/Timelapse.mp4", fourcc, 30, (width, height))
        loaded_imgs = load_imgs(current_files, loaded_imgs, width, height)
        write_video(video_obj, loaded_imgs)
        files_read = current_files

    def test_add_files(self):
        files_read = []
        loaded_imgs = []
        fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
        width, height = 720, 480

        current_files = ["SampleImages/img1.JPG"] * 100
        video_obj = VideoWriter("static/Timelapse.mp4", fourcc, 30, (width, height))
        loaded_imgs = load_imgs(current_files, loaded_imgs, width, height)
        write_video(video_obj, loaded_imgs)
        files_read = current_files

        current_files= ["SampleImages/img1.JPG"]*100+["SampleImages/img2.JPG"]*100

        video_obj = VideoWriter("static/Timelapse.mp4", fourcc, 30, (width, height))
        new_files = current_files[len(files_read):]
        loaded_imgs = load_imgs(new_files, loaded_imgs, width, height)
        write_video(video_obj, loaded_imgs)
        files_read = files_read + new_files
        print("Wrote new files")

if __name__ == '__main__':
    unittest.main()
