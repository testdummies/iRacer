#https://pymotw.com/2/ConfigParser/
from ConfigParser import SafeConfigParser
import time
from datetime import datetime
import pygame
import time, sys

pygame.init()
pygame.display.set_mode((1,1))

parser = SafeConfigParser()
parser.read('iRacer.config')
for section in ['Keyboard_mapping', 'Controller_mapping']:
    print '%s section exists: %s' % (section, parser.has_section(section))
    for candidate in [ 'Steer Left', 'Steer Right', 'Accelerate', 'Break/Reverse', 'Hand Break', 'N.O.S', 'Transmission', 'Gear Up', 'Gear Down','Cruise Control','Record Movements On','Record Movements Off']:
        print '%s.%-12s  : %s' % (section, candidate, parser.has_option(section, candidate))
    print


#Controls correspoding to the GUI optiosn. Array to store both keyboard and controller
control_SL      = []
control_SR      = []
control_A       = []
control_BR      = []
control_HB      = []
control_NOS     = []
control_Tran    = []
control_GU      = []
control_GD      = []

control_CC      = []
control_RM_On   = []
control_RM_Off  = []
#==========================================================================

pygame.key.set_repeat(1,125)        # this repeats keys to replace our
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print event.key
            print pygame.key.name(event.key)

'''
control_SL.append(parser.get('Keyboard_mapping', 'Steer Left'))
control_SL.append(parser.get('Controller_mapping', 'Steer Left'))


print control_SL
'''
