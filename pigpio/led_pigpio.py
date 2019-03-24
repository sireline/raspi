from time import sleep
import pigpio

pig = pigpio.pi()
pig.set_mode(21, pigpio.OUTPUT)
pig.set_mode(4, pigpio.INPUT)
pig.set_pull_up_down(4, pigpio.PUD_DOWN)

def cbf(gpio, level, tick):
    print(gpio, level, tick)

cb = pig.callback(4, pigpio.RISING_EDGE, cbf)

try:
    while True:
        sleep(1)
        pig.write(21, 1)
        sleep(1)
        pig.write(21, 0)
        sleep(1)
except KeyboardInterrupt:
    pig.stop()
