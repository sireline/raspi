from time import sleep

import pigpio
from BMX055 import bmx055

bmx = bmx055()
bmx.setup()

try:
    while True:
        print(bmx.read_accel())
        sleep(1)
except KeyboardInterrupt:
    bmx.stop()
