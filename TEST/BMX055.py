import smbus
import time, math

class bmx055:
    def __init__( self, i2c, accel_addr, comp_addr, gyro_addr ):
        self.accel_addr = accel_addr
        self.comp_addr = comp_addr
        self.gyro_addr = gyro_addr
        self.i2c = i2c
        
        self.i2c.write_byte_data( self.accel_addr, 0x0f, 0x03 )
        time.sleep(0.1)

        self.i2c.write_byte_data( self.accel_addr, 0x10, 0x08 )
        time.sleep(0.1)

        self.i2c.write_byte_data( self.accel_addr, 0x11, 0x00 )
        time.sleep(0.1)
        
        self.i2c.write_byte_data( self.gyro_addr, 0x0f, 0x04 )
        time.sleep(0.1)
        
        self.i2c.write_byte_data( self.gyro_addr, 0x10, 0x07 )
        time.sleep(0.1)

        self.i2c.write_byte_data( self.gyro_addr, 0x11, 0x00 )
        time.sleep(0.1)

        self.i2c.write_byte_data( self.comp_addr, 0x4b, 0x83 )
        time.sleep(0.1)

        self.i2c.write_byte_data( self.comp_addr, 0x4b, 0x01 )
        time.sleep(0.1)

        self.i2c.write_byte_data( self.comp_addr, 0x4c, 0x00 )
        self.i2c.write_byte_data( self.comp_addr, 0x4e, 0x84 )
        self.i2c.write_byte_data( self.comp_addr, 0x51, 0x04 )
        self.i2c.write_byte_data( self.comp_addr, 0x52, 0x16 )

        time.sleep(0.3)

    def read_accel( self ):
        x_l = self.i2c.read_byte_data( self.accel_addr, 0x02 )
        x_m = self.i2c.read_byte_data( self.accel_addr, 0x03 )
        y_l = self.i2c.read_byte_data( self.accel_addr, 0x04 )
        y_m = self.i2c.read_byte_data( self.accel_addr, 0x05 )
        z_l = self.i2c.read_byte_data( self.accel_addr, 0x06 )
        z_m = self.i2c.read_byte_data( self.accel_addr, 0x07 )

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
        x_l = self.i2c.read_byte_data( self.comp_addr, 0x42 )
        x_m = self.i2c.read_byte_data( self.comp_addr, 0x43 )
        y_l = self.i2c.read_byte_data( self.comp_addr, 0x44 )
        y_m = self.i2c.read_byte_data( self.comp_addr, 0x45 )
        z_l = self.i2c.read_byte_data( self.comp_addr, 0x46 )
        z_m = self.i2c.read_byte_data( self.comp_addr, 0x47 )
        t_l = self.i2c.read_byte_data( self.comp_addr, 0x48 )
        t_m = self.i2c.read_byte_data( self.comp_addr, 0x49 )

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
        x_l = self.i2c.read_byte_data( self.gyro_addr, 0x02 )
        x_m = self.i2c.read_byte_data( self.gyro_addr, 0x03 )
        y_l = self.i2c.read_byte_data( self.gyro_addr, 0x04 )
        y_m = self.i2c.read_byte_data( self.gyro_addr, 0x05 )
        z_l = self.i2c.read_byte_data( self.gyro_addr, 0x06 )
        z_m = self.i2c.read_byte_data( self.gyro_addr, 0x07 )

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
