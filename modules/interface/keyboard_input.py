# TODO THIS SECTION
import pygame
import modules.movement.control as control

pygame.init()
pygame.display.set_mode((50, 50))


def check_active_keys():

    for event in pygame.event.get():  # for every event in queue
        if event.type == (pygame.KEYDOWN or pygame.KEYDOWN):  # if event type is keyboard key down or key up
            pressed_list = pygame.key.get_pressed()  # execute following

    transmission = "Automatic"
    steer_left = are_keys_in_list(pressed_list, key_list)
    steer_right = are_keys_in_list(pressed_list, key_list)
    accelerate = are_keys_in_list(pressed_list, key_list)
    break_reverse = are_keys_in_list(pressed_list, key_list)
    hand_break = are_keys_in_list(pressed_list, key_list)
    NOS = are_keys_in_list(pressed_list, key_list)
    Gear_Up = are_keys_in_list(pressed_list, key_list)
    Gear_Down = are_keys_in_list(pressed_list, key_list)
    Cruise_Control = are_keys_in_list(pressed_list, key_list)
    Record_Movements_On = are_keys_in_list(pressed_list, key_list)
    Record_Movements_Off = are_keys_in_list(pressed_list, key_list)


    if (hand_break):
        control.current_direction = 0
        control.current_gear = 0

    else:
        control.current_direction = update_current_direction(steering_change(steer_left, steer_right))
        if transmission == "Automatic":
            control.current_gear = update_current_gear(control.current_gear, acceleration_change(accelerate, break_reverse))
        if transmission == "Manual":
            control.current_gear = update_current_gear(control.current_gear, gear_change(Gear_Up, Gear_Down))


def are_keys_in_list(list_of_pressed, key_list):

    for key in key_list:
        if list_of_pressed[key]:
            return True
    return False

def update_current_direction(change_to_direction):
    return change_to_direction  # returns current direction if 0 straight, if -1 left if 1 right.


def update_current_gear(current_gear, change_to_gear):

    tmp = current_gear + change_to_gear

    if tmp < 0:
        return -1       # limits reverse gear to -1
    if tmp > 5:
        return 5        # limits accelerate gears to 5


def steering_change(left, right):
    if left and right:
        return 0        # both keys pressed no change in movement
    elif left:
        return -1       # left steering is pressed move to left
    elif right:
        return 1        # right steering is pressed move to right
    else:
        return 0        # nothing is pressed return no change


def acceleration_change(forward, reverse):
    if forward and reverse:
        return 0        # both keys pressed no change in movement
    elif forward:
        return 1        # forward acceleration pressed
    elif reverse:
        return -1       # reverse acceleration pressed
    else:
        return 0        # nothing is pressed return no change

def gear_change(Gear_Up, Gear_Down):
    change_to_gear = 0
    if Gear_Up and Gear_Down:
        change_to_gear += 0
    elif Gear_Up:
        change_to_gear += 1
    elif Gear_Down:
        change_to_gear += -1

    if (control.current_gear + change_to_gear)<0:
        return -1
    if (control.current_gear + change_to_gear) > 5:
        return 5



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






