from time import sleep

from SERVO import SERVO

# hpwm---------------------------------------
# gsw: min=31500, center=67000, max=150000
# sg92r: min=50000, center=75000, max=100000 
# ===========================================

#gsw = SERVO(12)
sg92r = SERVO(12)

try:
    while True:
        for i in range(3, 14):
            sg92r.hpwm(50, i*10000)
            sleep(1)


#        sg92r.move(0)
#        sg92r.hpwm(50, 30000)
#        sleep(1)
#        sg92r.hpwm(50, 70000)
#        sg92r.move(1450)
#        sleep(1)
#        sg92r.hpwm(50, 130000)
#        sg92r.move(2500)
#        sleep(1)

#        gsw.hpwm(50, 31500)
#        sleep(1)
#        gsw.hpwm(50, 67000)
#        sleep(1)
#        gsw.hpwm(50, 150000)
#        sleep(1)
except KeyboardInterrupt:
    sg92r.stop()
    sg92r.clear()

#    gsw.stop()
#    gsw.clear()
