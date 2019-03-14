# -*- coding: utf-8 -*-
from time import sleep
import smbus

class ST7032:
    def __init__(self, view_speed=0.5):
        # I2C Device Settings
        self.bus = smbus.SMBus(1)
        self.address_st7032 = 0x3e
        self.register_setting = 0x00
        self.register_display = 0x40

        self.contrast = 36 # 0から63のコントラスト。30から40程度を推奨
        self.chars_per_line = 8 # LCDの横方向の文字数
        self.display_lines = 2   # LCDの行数

        self.display_chars = self.chars_per_line * self.display_lines

        self.position = 0
        self.line = 0
        self.view_speed = view_speed
        
    def setup_st7032(self):
        trials = 5
        for i in range(trials):
            try:
                c_lower = (self.contrast & 0xf)
                c_upper = (self.contrast & 0x30)>>4
                self.bus.write_i2c_block_data(self.address_st7032, self.register_setting, [0x38, 0x39, 0x14, 0x70|c_lower, 0x54|c_upper, 0x6c])
                sleep(0.2)
                self.bus.write_i2c_block_data(self.address_st7032, self.register_setting, [0x38, 0x0d, 0x01])
                sleep(0.001)
                break
            except IOError:
                if i==trials-1:
                    sys.exit()

    def clear(self):
        self.position = 0
        self.line = 0
        self.bus.write_byte_data(self.address_st7032, self.register_setting, 0x01)
        sleep(0.001)

    def newline(self):
        if self.line == self.display_lines-1:
            self.clear()
        else:
            self.line += 1
            self.position = self.chars_per_line * self.line
            self.bus.write_byte_data(self.address_st7032, self.register_setting, 0xc0)
            sleep(0.001)

    def write_string(self, s):
        for c in list(s):
            self._write_char(ord(c))
            sleep(self.view_speed)

    def _write_char(self, c):
        byte_data = self._check_writable(c)
        if self.position == self.display_chars:
            self.clear()
        elif self.position == self.chars_per_line * (self.line+1):
            self.newline()
        self.bus.write_byte_data(self.address_st7032, self.register_display, byte_data)
        self.position += 1

    def _check_writable(self, c):
        c = self._kana_conv(c)
        if c >= 0x06 and c <= 0xff :
            return c
        else:
            return 0x20 # 空白文字

    def _kana_conv(self, c):
        """
        {'ｦ': 0xff66, ..., 'ﾟ': 0xff9f} to {'ｦ': 0xa6, ..., 'ﾟ': 0xdf}
        kana = ['ｦ', 'ｧ', 'ｨ', 'ｩ', 'ｪ', 'ｫ', 'ｬ', 'ｭ', 'ｮ', 'ｯ', 'ｰ', 'ｱ', 'ｲ', 'ｳ', 'ｴ', 'ｵ', 'ｶ', 'ｷ', 'ｸ', 'ｹ', 'ｺ', 'ｻ', 'ｼ', 'ｽ', 'ｾ', 'ｿ', 'ﾀ', 'ﾁ', 'ﾂ', 'ﾃ', 'ﾄ', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ', 'ﾉ', 'ﾊ', 'ﾋ', 'ﾌ', 'ﾍ', 'ﾎ', 'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ', 'ﾔ', 'ﾕ', 'ﾖ', 'ﾗ', 'ﾘ', 'ﾙ', 'ﾚ', 'ﾛ', 'ﾜ', 'ﾝ', 'ﾞ', 'ﾟ']
        if chr(c) in kana:
            return c - 0xfec0
        else:
            return c

        """
        if 0xff66 <= c <= 0xff9f:
            return c - 0xfec0
        else:
            return c
