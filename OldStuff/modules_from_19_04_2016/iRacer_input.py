import pygame

from OldStuff.modules_from_19_04_2016 import iRacer_controls

#CONTROLS

#CAR CONTROLS
#Steer Left     -DONE
#Steer Right    -DONE
#Accelerate     -DONE
#Break/Reverse  -DONE
#Hand Break
#N.O.S
#Transmission Type
#Gear Up        -DONE
#Gear Down      -DONE

#IDEA is that if you press buttons that result in opposite reaction it cancels the action out
#because of this we will need three states,
#-1 corresponding to One action
# 0 corresponding to no change
#1 corresponding to Second action

#Due to Nature of the car speeds in both direction are exactly the same, unlike
#real cars where reverse has only one gear (speed range), it i]





# Name:       speed_lookup(inputValue):
# Arguments:  inputValue is a decimal value for speed 1-10.
# Purpose:    Looks up hexadecimal value using decimal input as a key
# Example:    inputValue = 10, return = '\x0F'

#---------------------------------------------------------------------
# Name:       set_acceleration():
# Purpose:    sets acceleration direction to forward or reverse
# Example:    acceleration = 1 is forward , acceleration = -1 is reverse,



pygame.init()
pygame.display.set_mode((1,1))


acceleration = 0
direction  = 0

import pygame

pygame.init()
pygame.display.set_mode((1,1))

pressed_forward = ord('w')
pressed_reverse = ord('s')
pressed_left = ord('a')
pressed_right = ord('d')


def set_acceleration(accelerate_forward,accelerate_reverse):
    #Accereration
    acceleration = 0
    if accelerate_forward:
        acceleration +=1
    if accelerate_reverse:
        acceleration -=1
    #print "acceleration: "+ str(acceleration)
    return acceleration

def set_steering(direction_right,direction_left):
    #Accereration
    direction = 0
    if direction_right:
        direction +=1
    if direction_left:
        direction -=1
    #print "direction: "+ str(direction)
    return direction

def set_gear(current_speed):
    #Accereration
    speed = current_speed
    if gear_shift_up:
        speed +=1
    if gear_shift_down:
        speed -=1
    return speed

def set_NOS(current_speed):
    #Accereration
    speed = current_speed
    speed += 5
    if speed > 10:
        speed =10
    return speed

def start_keyboard_input():
    pygame.key.set_repeat(1,125)        # this repeats keys to replace our
    while True:
        for event in pygame.event.get():
            keyPressed = pygame.key.get_pressed()
            accelerate_forward = False
            accelerate_reverse = False
            direction_right = False
            direction_left = False

            if keyPressed[pressed_forward] and keyPressed[pressed_reverse]:
                accelerate_forward = True
                accelerate_reverse = True
            elif keyPressed[pressed_forward]:
                accelerate_forward = True
                accelerate_reverse = False
            elif keyPressed[pressed_reverse]:
                accelerate_reverse = True
                accelerate_forward = False

            if keyPressed[pressed_left] and keyPressed[pressed_right]:
                direction_right = True
                direction_left = True
            elif keyPressed[pressed_left]:
                direction_right = False
                direction_left = True
            elif keyPressed[pressed_right]:
                direction_right = True
                direction_left = False

            speed_change = 2
            acceleration_change = set_acceleration(accelerate_forward,accelerate_reverse) # number 1,0 or -1
            steering_change = set_steering(direction_right,direction_left) # number 1,0 or -1
            acc = iRacer_controls.current_acceleration
            ster = iRacer_controls.current_steering
            print "Acceleration: %-*s  Steering: %s" % (20,str(acc),str(ster))
            iRacer_controls.change_current_stats(speed_change, acceleration_change, steering_change)

            command = iRacer_controls.input_to_movement(acc, ster, 2)
            iRacer_controls.car_drive(command, 0.1)


def get_code(time,direction,speed):
    #send commands#
    #dir_hex = '\x10'
    #speed_hex = '\x05'
    time = 5

    direction = iRacer_controls.direction_lookup("Dir_SF")
    speed = iRacer_controls.speed_lookup(4)

    value = iRacer_controls.combine_inputs(direction, speed)
    iRacer_controls.car_drive(value, time)


def sending_Commands(time,direction,speed):
    #send commands#
    #dir_hex = '\x10'
    #speed_hex = '\x05'
    time = 5

    direction = iRacer_controls.direction_lookup("Dir_SF")
    speed = iRacer_controls.speed_lookup(4)

    value = iRacer_controls.combine_inputs(direction, speed)
    iRacer_controls.car_drive(value, time)


#Direction

def input_example():
    print "input_example"
