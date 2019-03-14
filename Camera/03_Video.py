import RPi.GPIO as GPIO
from picamera import PiCamera
from time import strftime
from time import sleep

PAUSE_TIME = 10
VIDEO_SAVE_DIR = '/home/pi/MyProjects/raspi/Camera/videos/'
FILE_NAME_FMT = '%Y-%m-%d_%H-%M-%S'

camera = PiCamera()
camera.resolution = (800, 600)
camera.start_preview(alpha=200)
camera.start_recording(VIDEO_SAVE_DIR + strftime(FILE_NAME_FMT) + '.h264')
sleep(PAUSE_TIME)
camera.stop_recording()
camera.stop_preview()
