import RPi.GPIO as GPIO
from time import sleep

def eve_sw(ch):
    print('SW pushed: ', GPIO.input(24))
    GPIO.output(25, not GPIO.input(25))
    print('GPIO(25) status: ', GPIO.input(25))

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.IN)
GPIO.add_event_detect(24, GPIO.RISING, callback=eve_sw, bouncetime=200)

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
