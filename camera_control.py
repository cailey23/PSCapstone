from typing import Tuple

import gphoto2 as gp

camera = None #This is currently set using global variables and thus it cannot work with multiple cameras.


def reconnect():
    is_connected = False
    while not is_connected:
        try:
            global camera
            camera = gp.Camera()
            camera.init()
            return
        except gp.GPhoto2Error as e:
            if "[-105]" not in str(e):
                raise e


def capture_image(image_file):
    reconnect()
    global camera
    try:
        path = camera.capture(gp.GP_CAPTURE_IMAGE)
        camera_file = camera.file_get(path.folder, path.name, gp.GP_FILE_TYPE_NORMAL)
        camera_file.save(image_file)
        camera.file_delete(path.folder, path.name)
    except gp.GPhoto2Error as e:
        print("Camera is disconnected")
        camera = reconnect()


def disconnect_camera():
    reconnect()
    global camera
    camera.exit()


def get_settings(*settings: str):
    reconnect()
    # initialize camera
    global camera
    # Get current configuration
    config = camera.get_config()

    settings_pairs = {}
    for setting in settings:
        settings_pairs[setting] = config.get_child_by_name(setting)

    return settings_pairs


def set_settings(*settings_values: Tuple[str, object]):
    reconnect()
    global camera
    config = camera.get_config()
    for setting, value in settings_values:
        config.set_child_by_name(setting, value) #I have no idea if this works
