import modules.bluetooth_controls as bt
import modules.calculations.math as math
import time


# ==============================================================================
# Global variables
# =============================Global variables=================================
current_direction = ""
current_gear = 0
current_command = ""


# =============================================================================
# Name:       set_current_direction()
# Purpose:    Sets current_direction to a string corresponding to correct input
# TODO        FINISH THIS UP
# =============================================================================
def set_current_direction(direction):
    global current_direction
    pass

# =============================================================================
# Name:       set_current_gear()
# Purpose:    Sets current_gear to a number corresponding to correct input
# TODO        FINISH THIS UP
# =============================================================================
def set_current_gear(gear):
    print ("inide set"+str(gear))
    global current_gear
    current_gear = gear


# =============================================================================
# Name:       update_command()
# Purpose:    takes currently set values for direction and gear to
#             convert it into current_command
# =============================================================================
def set_current_command():
    global current_command
    current_command = math.get_combined_value(current_direction, current_gear)


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

