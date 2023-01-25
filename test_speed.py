"""
Tests the speed of different number of images:

The current speeds of the time lapse are as follows:
Initialize 0 Images:        .002 s
Initialize 1 Image:         .233 s
Initialize 100 Images:      23 s
Initialize 1000 Images:     248 s
Initialize 24000 Images:    3 hours 11 minutes

The second time is a time based on around using the time for initialize. It may not be the most accurate and the code
should probably be modified to print out the times within itself
Append 50 Images:           12 s, ~12 s for appending
Append 50 images x2:        24 s, ~12 s for appending
Append 500 Images:          57 s, ~57 s for appending
Append 10 Images to 1000:   262 s, ~14 s for appending
Append 10 Images to 24000:  3 hours 15 minutes, ~4 minutes for appending

The speed of the time lapse command line are as follows:
Initialize 50:              20 s
Append 50 to 50:            40 s

Init 50 sh:                 20 s
Append 50 to 50 sh:         40 s
"""
import unittest

from TimeLapse import TimeLapse
from TimeLapseCL import initialize_video, append_video, init_sh, append_sh


class TimeLapseST(unittest.TestCase):
    def test_initialize_0_images(self):
        time_lapse=TimeLapse("SampleImages")
        current_files = []
        time_lapse.initialize_video(current_files)

    def test_initialize_1_image(self):
        time_lapse = TimeLapse("SampleImages")
        current_files = ["SampleImages/img_0001.JPG"]
        time_lapse.initialize_video(current_files)

    def test_initialize_100_images(self):
        time_lapse = TimeLapse("SampleImages")
        current_files = ["SampleImages/img_0001.JPG"] * 100
        time_lapse.initialize_video(current_files)

    def test_initialize_1000_images(self):
        time_lapse = TimeLapse("SampleImages")
        current_files = ["SampleImages/img_0001.JPG"] * 1000
        time_lapse.initialize_video(current_files)

    def test_append_50_images(self):
        time_lapse = TimeLapse("SampleImages")
        current_files = ["SampleImages/img_0001.JPG"]
        time_lapse.initialize_video(current_files)
        current_files = ["SampleImages/img_0001.JPG"] * 51
        time_lapse.append_video(current_files)

    def test_append_50_images_x2(self):
        time_lapse = TimeLapse("SampleImages")
        current_files = ["SampleImages/img_0001.JPG"]
        time_lapse.initialize_video(current_files)
        current_files = ["SampleImages/img_0001.JPG"] * 51
        time_lapse.append_video(current_files)
        current_files = ["SampleImages/img_0001.JPG"] * 101
        time_lapse.append_video(current_files)

    def test_append_500_images(self):
        time_lapse = TimeLapse("SampleImages")
        current_files = ["SampleImages/img_0001.JPG"]
        time_lapse.initialize_video(current_files)
        current_files = ["SampleImages/img_0001.JPG"] * 501
        time_lapse.append_video(current_files)

    def test_append_10_images_to_1000(self):
        time_lapse = TimeLapse("SampleImages")
        current_files = ["SampleImages/img_0001.JPG"] * 1000
        time_lapse.initialize_video(current_files)
        current_files = ["SampleImages/img_0001.JPG"] * 1010
        time_lapse.append_video(current_files)

    def test_initialize_24000_images(self):
        time_lapse = TimeLapse("SampleImages")
        current_files = ["SampleImages/img_0001.JPG"] * 24000
        time_lapse.initialize_video(current_files)

    def test_append_10_images_to_24000(self):
        time_lapse = TimeLapse("SampleImages")
        current_files = ["SampleImages/img_0001.JPG"] * 24000
        time_lapse.initialize_video(current_files)
        current_files = ["SampleImages/img_0001.JPG"] * 24010
        time_lapse.append_video(current_files)


class TimeLapseCLST(unittest.TestCase):
    #This is slower than what exists
    def test_initialize_ffmpeg_50_images(self):
        initialize_video("static/TimeLapse.mp4", "SampleImages/img_%04d.JPG",720, 480, 30)

    def test_append_ffmpeg_50_images_x2(self):
        initialize_video("static/TimeLapse.mp4", "SampleImages/img_%04d.JPG", 720, 480, 30)
        append_video("static/TimeLapse.mp4", "SampleImages/img_%04d.JPG",720, 480, 30, 0)

    def test_initialize_sh_50_images(self):
        init_sh()


    def test_append_sh_50_images_x2(self):
        init_sh()
        append_sh()


if __name__ == '__main__':
    unittest.main()
