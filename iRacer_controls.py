import iRacer_bluetooth
import iRacer_recorder #recorder to be used for recording movements
import time
import struct

debugging = False

# Program parameters.
#
# Control Bytes are Constructed in Hex like this:
# 0xXY - Where X is the direction and Y is the speed.
# By using most significant bit for direction and least significant bit for speed,
# hexadecimal addition can be performed to receive hex value that will correspond
# to both direction and speed as single byte in 0xXY format.
#
# ORIGINAL DESCRIPTION:
# DIRECTION:
#
# Variable:     Description:                Code:
# Dir_Stop    = Stop                        0x0Y
# Dir_SF      = Straight / Forward          0x1Y
# Dir_SB      = Straight / Backward         0x2Y
#
# Dir_LN      = Left / No Drive             0x3Y
# Dir_LN      = Right / No Drive            0x4Y
#
# Dir_LF      = Left / Forward              0x5Y
# Dir_RF      = Right / Forward             0x6Y
#
# Dir_LB      = Left / Backward             0x7Y
# Dir_RB      = Right / Backward            0x8Y
#
# Dir_Active = One of the other variables

# SPEED:
#
# Variable:     Description:                Code:
# Spd_Stop    = Stop                        0xX0
# Spd_01      = Slowest                     0xX1
# Spd_02      = Way Way Slow                0xX2
# Spd_03      = Way Slow                    0xX3
# Spd_04      = LessWaySlow                 0xX4
# Spd_05      = Slow                        0xX5
# Spd_06      = Easy-Going                  0xX6
# Spd_07      = Cruising                    0xX7
# Spd_08      = Moving Right long           0xX8
# Spd_09      = Moving Quick                0xX9
# Spd_10      = Moving Quicker              0xXA
# Spd_11      = Moving Pretty Darn Quick    0xXB
# Spd_12      = Fast                        0xXC
# Spd_13      = Faster                      0xXD
# Spd_14      = Fastest                     0xXE
# Spd_15      = I lied,this is fastest      0xXF
# NOTE Speeds 1-5 Do not work - Adjusted to start from 6


Direction = dict()
Direction["Dir_Stop"] = '\x00'
Direction["Dir_SF"] = '\x10'
Direction["Dir_SB"] = '\x20'
Direction["Dir_LN"] = '\x30'
Direction["Dir_RN"] = '\x40'
Direction["Dir_LF"] = '\x50'
Direction["Dir_RF"] = '\x60'
Direction["Dir_LB"] = '\x70'
Direction["Dir_RB"] = '\x80'

Speed = dict()
Speed[1] = '\x06'
Speed[2] = '\x07'
Speed[3] = '\x08'
Speed[4] = '\x09'
Speed[5] = '\x0A'
Speed[6] = '\x0B'
Speed[7] = '\x0C'
Speed[8] = '\x0D'
Speed[9] = '\x0E'
Speed[10] = '\x0F'

current_speed = 0               #just speed for now
current_acceleration = 0           #Forward - x10  #reverse x20
current_steering = 0    #LF -x50 LR-x60  LB-x70 RB-x80




def car_drive(command, duration):
    # takes combined input for direction/speed and makes car drive
    check_recording_status() # CHECK IF IT DOES NOT BREAK
    iRacer_bluetooth.send_command(command)
    time.sleep(duration)  # gives sleep of 50 miliseconds
    #car_stop()

def check_recording_status(): # CHECK IF IT DOES NOT BREAK
    if iRacer_recorder.car_recorder: #if recorder is on record
        iRacer_recorder.recorder(command, duration, timestamp) # generate values for recording
    if iRacer_recorder.car_player:
        iRacer_recorder.player() # generate values for recording


def car_record(command, duration): # CHECK IF IT DOES NOT BREAK
    timestamp = "temp value"
    iRacer_recorder.record(command, duration, timestamp) # to be sent to recorder.

def car_play(): # CHECK IF IT DOES NOT BREAK
    iRacer_recorder.play() # exeecutes saved recording


def car_stop():
    iRacer_bluetooth.send_command('\x00')  # sends stop


def car_cruise():
    # takes last input and contiunues to drive at contant speed -figure out how
    print "car_cruise"


def select_action(pressed_keys_list):
    print "selected_action"


def chose_inputs(direction, speed):
    print "chose_inputs"


# Name:       speed_lookup(inputValue):
# Arguments:  inputValue is a decimal value for speed 1-10.
# Purpose:    Looks up hexadecimal value using decimal input as a key
# Example:    inputValue = 10, return = '\x0F'
def speed_lookup(inputValue):
    if debugging:
        print "\n"
        print "\n"
        print "Method: speed_lookup(" + str(inputValue) + "):"
        print "Speed[inputValue]: " + str(Speed[inputValue])
    return Speed[inputValue]
#---------------------------------------------------------------------
#---------------------------------------------------------------------

# Name:       direction_lookup(inputValue):
# Arguments:  inputValue is a string corresponding to direction name.
# Purpose:    Looks up hexadecimal value using direction name as a key
# Example:    inputValue = "Dir_LN", return = '\x30'


def direction_lookup(inputValue):
    if debugging:
        print "\n"
        print "Method: direction_lookup(" + str(inputValue) + "):"
        print "Direction[inputValue]: " + str(Direction[inputValue])
    return Direction[inputValue]
#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Name:       combine_inputs(dir_hex,speed_hex)
# Arguments:  dir_hex = Hex value for Direction
#             speed_hex = Hex value for Speed
# Purpose:    Combines both Direction and Speed into single byte.
# Example:    Direction = \x30, Speed = \x09, return = \x39.


def combine_inputs(dir_hex, speed_hex):
    input_values = (hex_to_int(dir_hex), hex_to_int(speed_hex))
    combined_values = sum(input_values)
    command_in_hex = int_to_hex(combined_values)
    if debugging:
        print "\n"
        print "Method: combine_inputs(" + str(dir_hex) + "," + str(speed_hex) + "):"
        print "input_values: " + str(input_values)
        print "combined_values: " + str(combined_values)
        print "command_in_hex: " + str(command_in_hex)
    return command_in_hex
#---------------------------------------------------------------------
def change_current_stats(speed_change,acceleration_change,steering_change):
    global current_speed,current_acceleration,current_steering

    tmp_current_speed = current_speed + speed_change
    tmp_current_acceleration = current_acceleration + acceleration_change
    tmp_current_steering = current_steering + steering_change

    tmp_current_speed = 2
    if tmp_current_acceleration > 5:
        tmp_current_acceleration = 5
    if tmp_current_acceleration < -1:
        tmp_current_acceleration = -1

    if tmp_current_steering > 1:
        tmp_current_steering = 1
    if tmp_current_steering < -1:
        tmp_current_steering = -1

    current_speed = tmp_current_speed
    current_acceleration = tmp_current_acceleration
    current_steering = tmp_current_steering



def input_to_movement(acceleration,steering,speed):
    movement = '\x00'
    speed = '\x09'

    if acceleration > 0 and steering > 0: # forward right
        movement = '\x60'
    elif acceleration > 0 and steering < 0: # forward left
        movement = '\x50'
    elif acceleration > 0 and steering == 0: # forward straight
        movement = '\x10'


    elif acceleration < 0 and steering > 0: # reverse right
        movement = '\x80'
    elif acceleration < 0 and steering < 0: # reverse left
        movement = '\x70'
    elif acceleration < 0 and steering == 0: # reverse straight
        movement = '\x20'


    elif acceleration == 0 and steering > 0: # stopped right
        movement = '\x60'
        speed = '\x00'
    elif acceleration == 0 and steering < 0: # stopped left
        movement = '\x50'
        speed = '\x00'
    elif acceleration == 0 and steering == 0: # stopped straight
        movement = '\x10'
        speed = '\x00'

    command = combine_inputs(movement, speed)
    return command









#---------------------------------------------------------------------
#SHOULD MOVE THIS TO OTHER MODULE - math or miscellaneous or something
#---------------------------------------------------------------------
# Name:       int_to_hex(int_value)
# Arguments:  int_value = integer value
# Purpose:    Converts integer to hexadecimal byte in '\x00' format
# Example:    int_value = 0 converted = '\x00'
def int_to_hex(int_value):
    converted = struct.pack('1B', int_value)
    if debugging:
        print "\n"
        print "Method: int_to_hex(" + str(int_value) + "):"
        print "converted: " + str(converted)
    return converted
#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Name:       hex_to_int(hex_value)
# Arguments:  hex_value = hexadecimal byte code '\x00'
# Purpose:    Converts hexadecimal to integer.
# Example:    hex_value = '\x00' converted[0] = 0


def hex_to_int(hex_value):
    converted = struct.unpack('1B', hex_value)
    if debugging:
        print "\n"
        print "Method: hex_to_int(" + str(hex_value) + "):"
        print "converted: " + str(converted)
        print "converted[0]: " + str(converted[0])
    return converted[0]
#---------------------------------------------------------------------
#---------------------------------------------------------------------
