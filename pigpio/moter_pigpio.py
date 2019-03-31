from time import sleep

from MOTER import MOTER

class TwinMoter:
    def __init__(self):
        self.m_r = MOTER()
        self.m_l = MOTER(in1_pin=22, in2_pin=23)

    def drive(self):
        self.m_r.drive()
        self.m_l.drive()

    def back(self):
        self.m_r.back()
        self.m_l.back()

    def stop(self):
        self.m_r.stop()
        self.m_l.stop()

    def clear(self):
        self.m_r.clear()
        self.m_l.clear()


tm = TwinMoter()
tm.drive()
sleep(1)
tm.back()
sleep(1)
tm.stop()
tm.clear()
