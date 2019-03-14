import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

GPIO.output(25, GPIO.HIGH)
sleep(5)
GPIO.output(25, GPIO.LOW)

GPIO.cleanup()
