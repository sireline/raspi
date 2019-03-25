from time import sleep

import pigpio

class bmx055:
    def __init__(self):
        self.pi = pigpio.pi() 
        self.i2c_bus = 1 
        self.accel_addr = 0x19 
        self.accel = None 
        self.comp_addr = 0x13
        self.comp = None 
        self.gyro_addr = 0x69
        self.gyro = None 
        
    def open(self, i2c_addr):    
        return self.pi.i2c_open(self.i2c_bus, i2c_addr)

    def close(self, handle):
        self.pi.i2c_close(handle)

    def stop(self):
        self.close(self.accel)
#        self.close(self.comp)
#        self.close(self.gyro)
        self.pi.stop()

    def setup(self):
        self.accel = self.open(self.accel_addr) 
        self.pi.i2c_write_byte_data(self.accel, 0x0f, 0x03)
        sleep(0.1)
        self.pi.i2c_write_byte_data(self.accel, 0x10, 0x08)
        sleep(0.1)
        self.pi.i2c_write_byte_data(self.accel, 0x11, 0x00)
        sleep(0.1)
        
#        self.gyro = self.open(self.gyro_addr) 
#        self.pi.i2c_write_byte_data(self.gyro, 0x0f, 0x04)
#        sleep(0.1)
#        self.pi.i2c_write_byte_data(self.gyro, 0x10, 0x07)
#        sleep(0.1)
#        self.pi.i2c_write_byte_data(self.gyro, 0x11, 0x00)
#        sleep(0.1)

#        self.comp = self.open(self.comp_addr) 
#        self.pi.i2c_write_byte_data(self.comp, 0x4b, 0x83)
#        sleep(0.1)
#        self.pi.i2c_write_byte_data(self.comp, 0x4b, 0x01)
#        sleep(0.1)
#        self.pi.i2c_write_byte_data(self.comp, 0x4c, 0x00)
#        self.pi.i2c_write_byte_data(self.comp, 0x4e, 0x84)
#        self.pi.i2c_write_byte_data(self.comp, 0x51, 0x04)
#        self.pi.i2c_write_byte_data(self.comp, 0x52, 0x16)

        sleep(0.3)

    def read_accel(self):
        x_l = self.pi.i2c_read_byte_data(self.accel, 0x02)
        x_m = self.pi.i2c_read_byte_data(self.accel, 0x03)
        y_l = self.pi.i2c_read_byte_data(self.accel, 0x04)
        y_m = self.pi.i2c_read_byte_data(self.accel, 0x05)
        z_l = self.pi.i2c_read_byte_data(self.accel, 0x06)
        z_m = self.pi.i2c_read_byte_data(self.accel, 0x07)

        x = ( ( x_m * 256 ) + ( x_l & 0xf0 ) ) / 16
        if ( x > 2047 ):
            x = x - 4096
        y = ( ( y_m * 256 ) + ( y_l & 0xf0 ) ) / 16
        if ( y > 2047 ):
            y = y - 4096
        z = ( ( x_m * 256 ) + ( z_l & 0xf0 ) ) / 16
        if ( z > 2047 ):
            z = z - 4096

        return ( x, y, z )


    def read_compass( self ):
        x_l = self.pi.i2c_read_byte_data(self.comp, 0x42)
        x_m = self.pi.i2c_read_byte_data(self.comp, 0x43)
        y_l = self.pi.i2c_read_byte_data(self.comp, 0x44)
        y_m = self.pi.i2c_read_byte_data(self.comp, 0x45)
        z_l = self.pi.i2c_read_byte_data(self.comp, 0x46)
        z_m = self.pi.i2c_read_byte_data(self.comp, 0x47)
        t_l = self.pi.i2c_read_byte_data(self.comp, 0x48)
        t_m = self.pi.i2c_read_byte_data(self.comp, 0x49)

        x = ( x_m <<8 ) + ( x_l >>3 )
        if ( x > 4095 ):
            x = x - 8192
        y = ( y_m <<8 ) + ( y_l >>3 )
        if ( y > 4095 ):
            y = y - 8192
        z = ( x_m <<8 ) + ( z_l >>3 )
        if ( z > 16383 ):
            z = z - 32768

        return ( x, y, z )

    def read_gyro( self ):
        x_l = self.pi.i2c_read_byte_data(self.gyro, 0x02)
        x_m = self.pi.i2c_read_byte_data(self.gyro, 0x03)
        y_l = self.pi.i2c_read_byte_data(self.gyro, 0x04)
        y_m = self.pi.i2c_read_byte_data(self.gyro, 0x05)
        z_l = self.pi.i2c_read_byte_data(self.gyro, 0x06)
        z_m = self.pi.i2c_read_byte_data(self.gyro, 0x07)

        x = ( x_m * 256 ) + x_l
        if ( x > 32767 ):
            x = x - 65536
        y = ( y_m * 256 ) + y_l
        if ( y > 32767 ):
            y = y - 65536
        z = ( x_m * 256 ) + z_l
        if ( z > 32767 ):
            z = z - 65536

        return ( x, y, z )
