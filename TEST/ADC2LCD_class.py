# -*- coding: utf-8 -*-
import sys
from time import sleep
from ST7032 import ST7032
import spidev
from mcp3204 import mcp3204

# Initalize Settings

VIEW_SPEED = 0.35
lcd = ST7032(VIEW_SPEED)
lcd.setup_st7032()

# SPI Device Settings
SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

adc = mcp3204(SPI_CE, SPI_SPEED, VREF)

# Main
if len(sys.argv)==1:
    try:
        while True:
            lcd.clear()
            analog_value = adc.get_value(READ_CH)
            lcd.write_string('AnaVal'+chr(0x3a)+' '+str(analog_value))
            sleep(1)
    except KeyboardInterrupt:
        lcd.clear()
else:
    lcd.write_string(sys.argv[1])
#    print(sys.argv)
#    print(list(sys.argv[1][0]))
#    print([hex(ord(c)) for c in sys.argv[1]])
#    print([ord(c) for c in sys.argv[1]])
#    print([chr(n) for n in range(12354, 12436)])
#    print([chr(n) for n in range(65382, 65440)])
#    print([hex(n-0xfec0) for n in range(65382, 65440)])
