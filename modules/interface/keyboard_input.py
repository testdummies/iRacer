# TODO THIS SECTION
import pygame
import modules.bluetooth_controls.connection as bt
import modules.calculations.math as math
import time

pygame.init()
pygame.display.set_mode((50, 50))
'''
import modules.configuration.active_settings as st

st.load_config()

Steer_Left = ord(st.KEYBOARD_Steer_Left)
Steer_Right = ord(st.KEYBOARD_Steer_Right)
Accelerate = ord(st.KEYBOARD_Accelerate)
Break_Reverse = ord(st.KEYBOARD_Break_Reverse)
Hand_Break = ord(st.KEYBOARD_Hand_Break)
NOS = ord(st.KEYBOARD_NOS)
Gear_Up = ord(st.KEYBOARD_Gear_Up)
Gear_Down = ord(st.KEYBOARD_Gear_Down)
Cruise_Control = ord(st.KEYBOARD_Cruise_Control)
Record_Movements_On = ord(st.KEYBOARD_Record_Movements_On)
Record_Movements_Off = ord(st.KEYBOARD_Record_Movements_Off)

'''



def set_acceleration(accelerate_forward,accelerate_reverse):
    acceleration = 0
    if accelerate_forward:
        acceleration +=1
    if accelerate_reverse:
        acceleration -=1
    return acceleration


def set_steering(direction_right,direction_left):
    direction = 0
    if direction_right:
        direction +=1
    if direction_left:
        direction -=1
    return direction


##http://nullege.com/codes/search?cq=pygame.event.get
def listen_for_input():
    pygame.key.set_repeat(1, 125)
    lookup_key = ord('w')
    print lookup_key
    while True: # run until quit
        for event in pygame.event.get(): # for every event in queue
            if event.type == (pygame.KEYDOWN or pygame.KEYDOWN): #if event type is keyboard key down or key up
                pressed_list = pygame.key.get_pressed() #execure following
                print (get_list_of_pressed(pressed_list))
                #print pressed_list[lookup_key]
                #if pressed_list[lookup_key]:
                    #print("w was pressed - sleeping now for 5sec")
            if event.type == (pygame.JOYBUTTONDOWN or pygame.JOYBUTTONUP): # if joystick button down or up
                pass
            if event.type == (pygame.JOYAXISMOTION or pygame.JOYBALLMOTION or pygame.JOYHATMOTION): # if joystick button down or up
                pass

def pygame_num_to_char(key_num):
    key_name = pygame.key.name(key_num)
    return key_name

def pygame_char_to_num(key_name):
    pass

def get_list_of_pressed(pressed):

    index = 0
    list_of_pressed = []
    list_of_pressed_chars = []
    for value in pressed:
        if (value != 0):
            list_of_pressed.append(index)
            list_of_pressed_chars.append(pygame_num_to_char(index))
        index +=1
    #return list_of_pressed
    return list_of_pressed_chars






