# TODO THIS SECTION
import pygame

pygame.init()
pygame.display.set_mode((1,1))

# Initialize the joysticks
Joy0 = pygame.joystick.Joystick(0)
Joy0.init()
def startJoy():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYHATMOTION:
                hat = event.value
                # checks the first value in the tuple
                if hat[0] == 1:
                    print 'hatright'
                    print("event value axis 0: {}".format(hat))
                if hat[0] == -1:
                    print 'hatleft'
                    print("event value axis 0: {}".format(hat))

                if hat[1] == 1:
                    print 'hatup'
                    print("event value axis 0: {}".format(hat))

                if hat[1] == -1:
                    print 'hatdown'
                    print("event value axis 0: {}".format(hat))

startJoy()