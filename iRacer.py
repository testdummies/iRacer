
import time
import modules.bluetooth_controls.connection as bt
import modules.interface.keyboard_input as key
import pygame
import modules.movement.manoeuvres as mv
import modules.configuration.active_settings as settings

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


    # save time for reference
    # if hand break is on just stop
    # else read for direction and gears
    # manual gear change - gears stay same unless changed - cruise control like
    # the way it was seemed to work fine?
    # automatic gear change - gears increase and decrease automatically on repeat
    # if accelerate or decelerate is on
    # reset time for reference
    # else:
    # do nothing until
    # if time for reference is > 0.5 sec
    # decrease speed by 1 until 0
    # reset time for reference

#checkMovements()

def check_pressed_keys_settings():
    settings.load_config()
    bt.initialise_bluetooth_settings()
    bt.connect_bluetooth()
    key.check_active_keys()


check_pressed_keys_settings()

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

