import pigpio

class SERVO:

    def __init__(self, gpio_pin=18, min_spw=550, center_spw=1450, max_spw=2350):
        self.gpio_pin = gpio_pin
        self.min_spw = min_spw
        self.center_spw = center_spw
        self.max_spw = max_spw
        self.pi = pigpio.pi()
        self.pi.set_mode(self.gpio_pin, pigpio.OUTPUT)

    def move(self, pos):
        if pos < self.min_spw:
            self.pi.set_servo_pulsewidth(self.gpio_pin, self.min_spw)
        elif self.min_spw <= pos <= self.max_spw:
            self.pi.set_servo_pulsewidth(self.gpio_pin, pos) 
        else:
            self.pi.set_servo_pulsewidth(self.gpio_pin, self.max_spw)

    def stop(self):
        self.pi.set_servo_pulsewidth(self.gpio_pin, 0)

    def hpwm(self, hz=50, duty=100000):
        self.pi.hardware_PWM(self.gpio_pin, hz, duty)

    def clear(self):
        self.pi.stop()
