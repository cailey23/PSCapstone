import os
import shutil
from tkinter import messagebox


def check_free_space(num_images, drive_location, image_file_size=6 * 10 ** 6):
    """
    Checks to see if there is file space on the file
    returns false if there is not enough room on the drive for the images
    """
    total, used, free = shutil.disk_usage(drive_location)
    return free >= num_images * image_file_size


def check_mount(path):
    return os.path.ismount(path)


def check_write_permission(path):
    try:
        with open(path + "/tempfile.txt", "r") as f:
            f.write("temp")
        os.remove(path + "/tempfile.txt")
    except PermissionError:
        return False
    return True


def do_checks(drive_location, num_images):
    if not check_mount(drive_location):
        messagebox.showerror("Drive not Found", "Drive is not currently mounted, please replug the mount")
    elif not check_free_space(num_images, drive_location):
        messagebox.showerror("Space Missing", "There is not enough space on the drive to hold the images")
    elif not check_write_permission(drive_location):
        messagebox.showerror("Permissions", "You do not have read/write permission to write the files")


if __name__ == "__main__":
    do_checks("..", 50)
    do_checks("..", 50000000)
