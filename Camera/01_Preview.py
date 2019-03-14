from picamera import PiCamera
from time import sleep

PAUSE_TIME = 10

camera = PiCamera()
camera.rotation = 180
camera.start_preview(alpha=200)
sleep(PAUSE_TIME)
camera.stop_preview()
