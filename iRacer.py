import time

import modules.bluetooth_controls.connection as bt
import modules.interface.keyboard_input as key
import pygame
import modules.movement.manoeuvres as mv

def checkMovements():
    bt.initialise_bluetooth_settings()
    bt.connect_bluetooth()
    mv.circle_left()
    #mv.circle_right()
    #mv.parallel_parking_left_side()
    #mv.parallel_parking_right_side()
    #mv.three_point_turn_left()
    #mv.three_point_turn_right()
    #mv.turn_around_left()
    #mv.turn_around_right()

checkMovements()



'''
def compile_list_of_keys_names_and_ids():
    key_list = pygame.key.get_pressed()
    list_of_ascii_num = []
    list_of_common_names = []
    index = 0
    print "known_keys = dict()"
    for key in key_list:
        #list_of_ascii_num.append(index)
        #list_of_common_names.append(pygame.key.name(index))
        #print ("ASCII ID: "+str(index)+" Key Name: "+pygame.key.name(index))
        print ('known_keys["'+(pygame.key.name(index)).upper()+'"] = '+str(index))
        index += 1


compile_list_of_keys_names_and_ids()
bt.initialise_bluetooth_settings()
bt.connect_bluetooth()
key.start_keyboard_input()
bt.disconnect_bluetooth()
'''

