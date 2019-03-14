import spidev

class mcp3204:
    def __init__( self, ss, speed, vref ):
        self.ss = ss
        self.speed = speed
        self.vref = vref
        self.spi_bus = 0
        
        self.spi = spidev.SpiDev()
        self.spi.open( self.spi_bus, self.ss )
        self.spi.max_speed_hz = self.speed
        
        
    def get_value( self, ch ):
        command = ( 0xc0 | ( ch << 3 ) ) 
        data = self.spi.xfer2( [ command , 0x00, 0x00 ] )
        value = (  data[0] << 24 | data[1] << 16 | data[2] << 8 | data[2] )  >> 13
        return value

    def get_volt( self, value ):
        return value * self.vref / float( 4095 )


