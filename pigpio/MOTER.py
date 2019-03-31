import pigpio

class MOTER:

    def __init__(self, in1_pin=24, in2_pin=25, pwm_range=100, pwm_hz=1600):
        self.in1_pin = in1_pin
        self.in2_pin = in2_pin
        self.pwm_range = pwm_range 
        self.pwm_hz = pwm_hz 
        self.pi = pigpio.pi()
        
        self.pi.set_mode(self.in1_pin, pigpio.OUTPUT)
        self.pi.set_PWM_range(self.in1_pin, self.pwm_range) 
        self.pi.set_PWM_frequency(self.in1_pin, self.pwm_hz)

        self.pi.set_mode(self.in2_pin, pigpio.OUTPUT)
        self.pi.set_PWM_range(self.in2_pin, self.pwm_range) 
        self.pi.set_PWM_frequency(self.in2_pin, self.pwm_hz)

        print(self.pi.get_PWM_range(self.in1_pin), self.pi.get_PWM_frequency(self.in1_pin))


    def drive(self):
        self.pi.set_PWM_dutycycle(self.in1_pin, 0)
        self.pi.set_PWM_dutycycle(self.in2_pin, 75)

    def back(self):
        self.pi.set_PWM_dutycycle(self.in1_pin, 75)
        self.pi.set_PWM_dutycycle(self.in2_pin, 0)

    def stop(self):
        self.pi.set_PWM_dutycycle(self.in1_pin, 0)
        self.pi.set_PWM_dutycycle(self.in2_pin, 0)

    def clear(self):
        self.pi.stop()
