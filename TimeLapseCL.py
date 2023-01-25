from subprocess import call


def initialize_video(video: str, images: str, width: int, height: int, framerate: int):
    call(
        f"ffmpeg -r {framerate} -f image2 -s {width}x{height} -i {images} -vcodec libx264 -crf 25  -pix_fmt yuv420p {video} -y -loglevel quiet", shell=True)


def append_video(video: str, images: str, width: int, height: int, framerate: int, num_frames: int):
    print(f"ffmpeg -r {framerate} -f image2 -s {width}x{height} -start_number {num_frames} -i {images} -vcodec libx264 -crf 25  -pix_fmt yuv420p temp.mp4 -loglevel quiet -y")
    print(f"ffmpeg -f concat -i videos.txt -c copy {video} -y")
    call(
        f"ffmpeg -r {framerate} -f image2 -s {width}x{height} -start_number {num_frames} -i {images} -vcodec libx264 -crf 25  -pix_fmt yuv420p temp.mp4 -loglevel quiet -y", shell=True)
    call(f"ffmpeg -f concat -i videos.txt -c copy {video} -y", shell=True)

def init_sh():
    call("bash Init_video.sh", shell=True)

def append_sh():
    call("bash append_img.sh", shell=True)