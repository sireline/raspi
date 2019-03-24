from time import sleep
import subprocess
import smbus

import RPi.GPIO as GPIO
from RPLCD import CharLCD
from BMX055 import bmx055

accel_addr = 0x19
comp_addr = 0x13
gyro_addr = 0x69
i2c_channel = 1

i2c = smbus.SMBus(i2c_channel)
sensor = bmx055(i2c, accel_addr, comp_addr, gyro_addr)

def my_callback(channel):
    global state
    global lcd

    if channel==4:
        state = not state
        if state == GPIO.HIGH:
           print(str(channel)+'ON')
           lcd.write_string('Hello RasPi Zero\n\rChannel: '+str(channel)+'   ON ')
        else:
           print(str(channel)+'OFF') 
           lcd.write_string('Hello RasPi Zero\n\rChannel: '+str(channel)+'   OFF')
    elif channel==17:
        print('ｼｬｯﾄﾀﾞｳﾝ ｶｲｼ ｼﾏｽ')
        lcd.write_string('Hello RasPi Zero\n\rｼｬｯﾄﾀﾞｳﾝ ｶｲｼ ｼﾏｽ')
        sleep(2) 
        lcd.close(clear=True)
        GPIO.cleanup()
        args = ['sudo', 'poweroff']
        subprocess.Popen(args)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(4, GPIO.RISING, callback=my_callback, bouncetime=200)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(17, GPIO.RISING, callback=my_callback, bouncetime=200)

lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11])
lcd.write_string('Hello RasPi Zero')
sleep(2)
lcd.clear()

state = GPIO.LOW

try:
    while True:
        (x, y, z) = sensor.read_accel()
        print("----------------------------------------")
        print("Accel\tx:", x, "\ty:", y, "\tz:", z)
        (x, y, z) = sensor.read_compass()
#        print("Compass\tx:", x, "\ty:", y, "\tz:", z)
        (x, y, z) = sensor.read_gyro()
        print("Pitch\tx:", x, "\tRoll:", y, "\tYaw:", z)

        sleep(1)

except KeyboardInterrupt:
    pass

lcd.close(clear=True)
GPIO.cleanup()
