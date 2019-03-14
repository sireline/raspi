# -*- coding: utf-8 -*-
import sys
from time import sleep

import smbus
import spidev
from mcp3204 import mcp3204

def setup_st7032():
    trials = 5
    for i in range(trials):
        try:
            c_lower = (contrast & 0xf)
            c_upper = (contrast & 0x30)>>4
            bus.write_i2c_block_data(address_st7032, register_setting, [0x38, 0x39, 0x14, 0x70|c_lower, 0x54|c_upper, 0x6c])
            sleep(0.2)
            bus.write_i2c_block_data(address_st7032, register_setting, [0x38, 0x0d, 0x01])
            sleep(0.001)
            break
        except IOError:
            if i==trials-1:
                sys.exit()

def clear():
    global position
    global line
    position = 0
    line = 0
    bus.write_byte_data(address_st7032, register_setting, 0x01)
    sleep(0.001)

def newline():
    global position
    global line
    if line == display_lines-1:
        clear()
    else:
        line += 1
        position = chars_per_line*line
        bus.write_byte_data(address_st7032, register_setting, 0xc0)
        sleep(0.001)

def write_string(s):
    for c in list(s):
        write_char(ord(c))

def write_char(c):
    global position
    byte_data = check_writable(c)
    if position == display_chars:
        clear()
    elif position == chars_per_line*(line+1):
        newline()
    bus.write_byte_data(address_st7032, register_display, byte_data)
    position += 1

def check_writable(c):
    if c >= 0x06 and c <= 0xff :
        return c
    else:
        return 0x20 # 空白文字

# Initalize Settings

# I2C Device Settings
bus = smbus.SMBus(1)
address_st7032 = 0x3e
register_setting = 0x00
register_display = 0x40

contrast = 36 # 0から63のコントラスト。30から40程度を推奨
chars_per_line = 8 # LCDの横方向の文字数
display_lines = 2   # LCDの行数

display_chars = chars_per_line*display_lines

position = 0
line = 0

setup_st7032()

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
            clear()
            analog_value = adc.get_value(READ_CH)
            write_string('AnaVal'+chr(0x3a)+' '+str(analog_value))
            sleep(1)
    except KeyboadInterrupt:
        clear()
else:
    write_string(sys.argv[1])
