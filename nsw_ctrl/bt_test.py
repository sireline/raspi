import sys
from time import sleep

sys.path.append('/usr/lib/python3/dist-packages')

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1,1))
    pygame.display.set_caption('Test')
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    while True:
        events = pygame.event.get()
        for event in events:
#            if event.type == pygame.JOYBUTTONDOWN or event.type == JOYHATMOTION:
            print(event)
        sleep(0.1)

if __name__ == '__main__':
    main()
