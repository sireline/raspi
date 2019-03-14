from picamera import PiCamera
from time import strftime
from time import sleep

PAUSE_TIME = 3
PHOTO_SAVE_DIR = '/home/pi/MyProjects/raspi/Camera/pictures/'
FILE_NAME_FMT = '%Y-%m-%d_%H-%M-%S'

camera = PiCamera()
camera.rotation = 180
camera.resolution = (800, 600)
camera.start_preview(alpha=200)
sleep(PAUSE_TIME)
camera.capture(PHOTO_SAVE_DIR + strftime(FILE_NAME_FMT) + '.jpeg')
camera.stop_preview()
