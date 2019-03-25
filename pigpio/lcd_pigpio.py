from time import sleep

import pigpio
from RPLCD.pigpio import CharLCD

pi = pigpio.pi()

lcd = CharLCD(pi, cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11], pin_contrast=9)
lcd.write_string('Hello RasPi')
sleep(3)
lcd.clear()
lcd.write_string('Test LCD pigpio')
sleep(3)
lcd.close(clear=True)
pi.stop()
