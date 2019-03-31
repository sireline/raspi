from time import sleep

import pigpio
from BMX055 import bmx055

bmx = bmx055()
bmx.setup()

try:
    while True:
        ax, ay, az = bmx.read_accel()
#        print("accel: ax={0}, ay={1}, az={2}".format(ax, ay, az))

        gx, gy, gz = bmx.read_gyro()
#        print("gyro: gx={0}, gy={1}, gz={2}".format(gx, gy, gz))

        cx, cy, cz = bmx.read_compass()
#        print("comp: cx={0}, cy={1}, cz={2}".format(cx, cy, cz))

        msg = "|       |  x  |  y  |  z  |\n"
        msg += "| accel | "+str(ax)+" | "+str(ay)+" | "+str(az)+" |\n"
        msg += "| gyro  | "+str(gx)+" | "+str(gy)+" | "+str(gz)+" |\n"
        msg += "| comp  | "+str(cx)+" | "+str(cy)+" | "+str(cz)+" |\n"
        print(msg)
        sleep(0.5)
except KeyboardInterrupt:
    bmx.stop()
