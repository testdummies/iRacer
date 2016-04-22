# TODO THIS SECTION
import time
import pygame
import modules.movement.control as control
import modules.configuration.active_settings as st
import modules.configuration.key_translation as kt
import modules.bluetooth_controls.connection as bt
import modules.movement.manoeuvres as mv

pygame.init()
pygame.display.set_mode((800, 600))
#Joy0 = pygame.joystick.Joystick(0)
#Joy0.init()


def check_active_keys():
    transmission = st.Transmission
    if transmission == "AUTOMATIC":
        pygame.key.set_repeat(1, 50) #125 default
    else:
        pass

    control.set_acceleration_timer()
    while True:
        transmission = st.Transmission
        for event in pygame.event.get():  # for every event in queue
            if event.type == \
                    pygame.ACTIVEEVENT \
                    or event.type == pygame.MOUSEMOTION \
                    or event.type == pygame.MOUSEBUTTONDOWN \
                    or event.type == pygame.MOUSEBUTTONUP:
                # event.type == 1 or event.type == 4 or event.type == 5 or event.type == 6
                pass
                # pass as those events are not what we are looking for

            if event.type ==pygame.KEYUP \
                    or event.type == pygame.KEYDOWN:
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
                macro1 = are_keys_in_list(pressed_list, [st.KEYBOARD_MACRO1])
                macro2 = are_keys_in_list(pressed_list, [st.KEYBOARD_MACRO2])
                macro3 = are_keys_in_list(pressed_list, [st.KEYBOARD_MACRO3])
                macro4 = are_keys_in_list(pressed_list, [st.KEYBOARD_MACRO4])
                macro5 = are_keys_in_list(pressed_list, [st.KEYBOARD_MACRO5])
                macro6 = are_keys_in_list(pressed_list, [st.KEYBOARD_MACRO6])
                macro7 = are_keys_in_list(pressed_list, [st.KEYBOARD_MACRO7])
                macro8 = are_keys_in_list(pressed_list, [st.KEYBOARD_MACRO8])
                quit = are_keys_in_list(pressed_list, [st.KEYBOARD_quit])


                if quit:
                    control.current_direction = "STOP"
                    control.current_gear = 0
                    control.set_current_command()
                    bt.send_command(control.current_command, 0.01)
                    return
                elif hand_break:
                    control.current_direction = "STOP"
                    control.current_gear = 0
                    control.set_current_command()
                    bt.send_command(control.current_command, 0.01)
                elif macro1:
                    mv.circle_left()
                elif macro2:
                    mv.circle_right()
                elif macro3:
                    mv.parallel_parking_left_side()
                elif macro4:
                    mv.parallel_parking_right_side()
                elif macro5:
                    mv.three_point_turn_left()
                elif macro6:
                    mv.three_point_turn_right()
                elif macro7:
                    mv.turn_around_left()
                elif macro8:
                    mv.turn_around_right()

                else:
                    control.current_direction = update_current_direction(control.current_gear,
                                                                         steering_change(steer_left, steer_right))
                    if transmission == "MANUAL":
                        control.set_current_gear(
                            update_current_gear(
                                control.current_gear, acceleration_change(Gear_Up, Gear_Down)
                            )
                        )

                    elif transmission == "AUTOMATIC":
                        if accelerate or break_reverse:
                            acc = acceleration_change(accelerate, break_reverse)
                            control.set_acceleration_gear_count(acc)
                            if control.acceleration_gear_count % 10 == 0:
                                control.set_current_gear(
                                    update_current_gear(
                                        control.current_gear, acceleration_change(accelerate, break_reverse)
                                    )
                                )
                            else:
                                pass
                            control.set_acceleration_timer()
                        else:
                            control.set_acceleration_gear_count(-100)
            if event.type == pygame.JOYHATMOTION:
                hat = event.value
                steer_left = are_hats_in_list(hat[0], st.CONTROLLER_Steer_Left)
                steer_right = are_hats_in_list(hat[0], st.CONTROLLER_Steer_Right)
                accelerate = are_hats_in_list(hat[1], st.CONTROLLER_Accelerate)
                break_reverse = are_hats_in_list(hat[1], st.CONTROLLER_Break_Reverse)

                control.current_direction = update_current_direction(control.current_gear,
                                                                     steering_change(steer_left, steer_right))
                if accelerate or break_reverse:
                    acc = acceleration_change(accelerate, break_reverse)
                    control.set_acceleration_gear_count(acc)
                    if control.acceleration_gear_count % 10 == 0:
                        print control.acceleration_gear_count
                        control.set_current_gear(
                            update_current_gear(
                                control.current_gear, acceleration_change(accelerate, break_reverse)
                            )
                        )
                    else:
                        pass
                    control.set_acceleration_timer()
                else:
                    control.set_acceleration_gear_count(-100)


            #print ("current gear "+str(control.current_gear))
            #print ("gear count "+str(control.acceleration_gear_count))
            control.set_current_command()
            if transmission == "AUTOMATIC" and check_time():
                control.set_current_command()
                control.set_acceleration_timer()

            send_if_change_in_commands()
        if transmission == "AUTOMATIC" and check_time():
                control.set_current_command()
                control.set_acceleration_timer()
                send_if_change_in_commands()


def send_if_change_in_commands():
    if control.current_command != control.previous_command:
        control.set_previous_command_as_current_command  # set previous command
        bt.send_command(control.current_command, 0.01)
    else:  # if nothing changed
        pass


def check_time():
    diff = time.time() - control.acceleration_timer
    if diff > 0.4:
        if control.current_gear > 0:
            #control.set_current_gear(0)

            control.set_current_gear(
                update_current_gear(
                    control.current_gear, -1)
            )
        elif control.current_gear < 0:
            # control.set_current_gear(0)
            control.set_current_gear(
                update_current_gear(
                    control.current_gear, 1)
            )

        return True
    else:
        return False


def are_keys_in_list(list_of_pressed, key_list):

    for key in key_list:
        if list_of_pressed[kt.get_key_number(key)]:
            return True
    return False

def are_hats_in_list(hat_pos, key):
    tmpkey = int(key)
    tmphat = int(hat_pos)
    print type(key)
    print type(hat_pos)
    if tmpkey == tmphat:
            return True
    return False

def update_current_direction(current_gear,  change_to_direction):

    new_direction = "STOP";
    if current_gear > 0: # if it's going forward
        if change_to_direction == 1:
            new_direction = "FR"         # Forward Right
            pass
        elif change_to_direction == -1:
            new_direction = "FL"         # Forward Left              pass
        else:
            new_direction = "FS"         # Forward Straight
            pass
    if current_gear < 0: # if it's going reverse
        if change_to_direction == 1:
            new_direction = "RR"        # Reverse Right            pass
        elif change_to_direction == -1:
            new_direction = "RL"        # Reverse Left
            pass
        else:
            new_direction = "RS"        # Reverse Straight
            pass
    if current_gear == 0:               # if it's going stopped
        if change_to_direction == 1:
            new_direction = "NR"        # Neutral Right
            pass
        elif change_to_direction == -1:
            new_direction = "NL"        # Neutral Left
            pass
        else:
            # do nothing
            pass

    return new_direction  # returns current direction if 0 straight, if -1 left if 1 right.


def update_current_gear(current_gear, change_to_gear):
    tmp = current_gear + change_to_gear

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

    if (control.current_gear + change_to_gear)< 0:
        return -1
    if (control.current_gear + change_to_gear) > 5:
        return 5





