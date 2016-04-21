# TODO THIS SECTION
import pygame
import modules.movement.control as control
import modules.configuration.active_settings as st
import modules.configuration.key_translation as kt
pygame.init()
pygame.display.set_mode((50, 50))


def check_active_keys():
    counter = 0
    while True:
        #pygame.key.set_repeat(1, 125)
        transmission = st.Transmission
        for event in pygame.event.get():  # for every event in queue
            #if event.type == (pygame.KEYDOWN or pygame.KEYUP):  # if event type is keyboard key down or key up
            pressed_list = pygame.key.get_pressed()  # execute following
            steer_left = are_keys_in_list(pressed_list, [st.KEYBOARD_Steer_Left])
            steer_right = are_keys_in_list(pressed_list, [st.KEYBOARD_Steer_Right])
            accelerate = are_keys_in_list(pressed_list, [st.KEYBOARD_Accelerate])
            break_reverse = are_keys_in_list(pressed_list, [st.KEYBOARD_Break_Reverse])
            hand_break = are_keys_in_list(pressed_list, [st.KEYBOARD_Hand_Break])
            NOS = are_keys_in_list(pressed_list, [st.KEYBOARD_NOS])
            Gear_Up = are_keys_in_list(pressed_list, [st.KEYBOARD_Gear_Up])
            Gear_Down = are_keys_in_list(pressed_list, [st.KEYBOARD_Gear_Down])
            Cruise_Control = are_keys_in_list(pressed_list, [st.KEYBOARD_Cruise_Control])
            Record_Movements_On = are_keys_in_list(pressed_list, [st.KEYBOARD_Record_Movements_On])
            Record_Movements_Off = are_keys_in_list(pressed_list, [st.KEYBOARD_Record_Movements_Off])


            if (hand_break):
                print ("handbreak on")
                control.current_direction = 0
                control.current_gear = 0
            else:
                print ("not on handbreak")
                control.current_direction = update_current_direction(steering_change(steer_left, steer_right))
                if transmission == "AUTOMATIC":
                    print ("Automatic")
                    control.set_current_gear(
                        update_current_gear(
                            control.current_gear, acceleration_change(accelerate, break_reverse)
                        )
                    )

                   # print ("current gear"+str(control.set_current_gear()))
                if transmission == "MANUAL":
                    print ("Manual")
                    control.set_current_gear(update_current_gear(control.current_gear, gear_change(Gear_Up, Gear_Down)))


            print counter
            counter+=1
'''
            print(transmission)
            print(steer_left)
            print(steer_right)
            print(accelerate)
            print(break_reverse)
            print(hand_break)
            print(NOS)
            print(Gear_Up)
            print(Gear_Down)
            print(Cruise_Control)
            print(Record_Movements_On)
            print(Record_Movements_Off)
            '''

            #print counter
            #counter+=1

def are_keys_in_list(list_of_pressed, key_list):

    for key in key_list:
        if list_of_pressed[kt.get_key_number(key)]:
            return True
    return False

def update_current_direction(change_to_direction):
    return change_to_direction  # returns current direction if 0 straight, if -1 left if 1 right.


def update_current_gear(current_gear, change_to_gear):
    #print (type(current_gear))
    # print (type(change_to_gear))
    #if type(current_gear) != int:
       # current_gear = 0
       # print current_gear

    tmp = current_gear + change_to_gear

    print (tmp)
    # print (type(change_to_gear))
    if tmp < 0:
        return -1       # limits reverse gear to -1
    elif tmp > 5:
        return 5        # limits accelerate gears to 5
    else:
        return tmp


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






