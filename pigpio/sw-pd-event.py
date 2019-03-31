from time import sleep

import pigpio

pi = pigpio.pi()
pi.set_mode(21, pigpio.OUTPUT)
pi.set_mode(4, pigpio.INPUT)
pi.set_pull_up_down(4, pigpio.PUD_DOWN)

def cbf(gpio, level, tick):
    print(gpio, level, tick)
    pi.write(21, 1)
    sleep(0.5)
    pi.write(21, 0)

cb = pi.callback(4, pigpio.RISING_EDGE, cbf)

try:
    while True:
        sleep(0.5)
except KeyboardInterrupt:
    pi.stop()
