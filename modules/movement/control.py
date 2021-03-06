import modules.bluetooth_controls as bt
import modules.calculations.math as math
import time


# ==============================================================================
# Global variables
# =============================Global variables=================================
current_direction = "STOP"
current_gear = 0
current_command = math.int_to_hex(0)
previous_command = math.int_to_hex(0)
acceleration_timer = time.time()
acceleration_gear_count = 0


# =============================================================================
# Name:       set_current_direction()
# Purpose:    Sets current_direction to a string corresponding to correct input
# TODO        FINISH THIS UP
# =============================================================================
def set_current_direction(direction):
    global current_direction
    pass

# =============================================================================
# Name:       set_acceleration_gear_count(number)
# Purpose:    Sets current_direction to a string corresponding to correct input
# TODO        FINISH THIS UP
# =============================================================================
def set_acceleration_gear_count(number):
    global acceleration_gear_count
    if number == -100:
        acceleration_gear_count = 0
    else:
        acceleration_gear_count += number

# =============================================================================
# Name:       set_current_direction()
# Purpose:    Sets current_direction to a string corresponding to correct input
# TODO        FINISH THIS UP
# =============================================================================
def set_acceleration_timer():
    global acceleration_timer
    acceleration_timer = time.time()

# =============================================================================
# Name:       set_current_gear()
# Purpose:    Sets current_gear to a number corresponding to correct input
# TODO        FINISH THIS UP
# =============================================================================
def set_current_gear(gear):
    #print ("inide set"+str(gear))
    global current_gear
    current_gear = gear


# =============================================================================
# Name:       set_current_command()
# Purpose:    takes currently set values for direction and gear to
#             convert it into current_command
# =============================================================================
def set_current_command():
    #print (str(current_direction) + str(current_gear))
    #print ("setting current_command to: "+str(current_command))
    global current_command
    current_command = math.get_combined_value(current_direction, current_gear)

# =============================================================================
# Name:       set_previous_command_as_current_command()
# Purpose:    takes currently set values for direction and gear to
#             convert it into current_command
# =============================================================================
def set_previous_command_as_current_command():
    #print "current command as previous command"
    global previous_command
    previous_command = current_command


# =============================================================================
# Name:       drive(command, duration)
# Arguments:  command = a hex value that corresponds to combined speed and direction
# Purpose:    sends command to the bluetooth device
# =============================================================================
def drive(command, duration):
    # takes combined input for direction/speed and makes car drive
    # implement listening and recording of commands
    bt.send_command(command)
    time.sleep(duration)  # gives sleep of 50 milliseconds

