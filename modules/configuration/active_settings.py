#TODO LOAD SETTINGS FROM CONFIG FILE
#TODO MAKE SURE BOTH KEYBOARD AND CONTROLLER INPUT GET TREATED EQUALLY
#TODO MAKE SURE SETTINGS WORK WITH SOMETHING THAT INTERPRETS KEYS
#TODO MAKE METHODS TO UPDATE BINDINGS.INI FILE AS WELL AS ON THE FLY UPDATE PROGRAM SETTSING FROM THAT FILE.
#TODO MAKE METHODS TO CHECK IF KEYS ARE USED FOR SOMETHING ELSE AND UNBIND THEM.
#TODO SETTINGS LIKE VERBOSE

import ConfigParser
import pygame
#http://pastebin.com/GKbPFdNs - known keys

config = ConfigParser.ConfigParser()
candidates = ['modules\configuration\config.ini', '..\configuration\config.ini', 'config.ini']
correctPath = []
correctPath.extend(config.read(candidates)) #it choses path that is relevant to the current directory it's calling from.

# [DEVICE SETTINGS]
MAC_ADDRESS = ""
BLUETOOTH_CHANNEL = ""

# [DRIVE_SETTINGS]
Transmission = ""

# [KEYBOARD_MAPPING]
KEYBOARD_Steer_Left = ""
KEYBOARD_Steer_Right = ""
KEYBOARD_Accelerate = ""
KEYBOARD_Break_Reverse = ""
KEYBOARD_Hand_Break = ""
KEYBOARD_NOS = ""
KEYBOARD_Gear_Up = ""
KEYBOARD_Gear_Down = ""
KEYBOARD_Cruise_Control = ""
KEYBOARD_Record_Movements_On = ""
KEYBOARD_Record_Movements_Off = ""

# [CONTROLLER_MAPPING]
CONTROLLER_Steer_Left = ""
CONTROLLER_Steer_Right = ""
CONTROLLER_Accelerate = ""
CONTROLLER_Break_Reverse = ""
CONTROLLER_Hand_Break = ""
CONTROLLER_NOS = ""
CONTROLLER_Gear_Up = ""
CONTROLLER_Gear_Down = ""
CONTROLLER_Cruise_Control = ""
CONTROLLER_Record_Movements_On = ""
CONTROLLER_Record_Movements_Off = ""


def load_config():
    global MAC_ADDRESS, BLUETOOTH_CHANNEL, Transmission, KEYBOARD_Steer_Left, KEYBOARD_Steer_Right
    global KEYBOARD_Accelerate, KEYBOARD_Break_Reverse, KEYBOARD_Hand_Break, KEYBOARD_NOS, KEYBOARD_Gear_Up
    global KEYBOARD_Gear_Down, KEYBOARD_Cruise_Control, KEYBOARD_Record_Movements_On, KEYBOARD_Record_Movements_Off
    global CONTROLLER_Steer_Left, CONTROLLER_Steer_Right, CONTROLLER_Accelerate, CONTROLLER_Break_Reverse, CONTROLLER_Hand_Break
    global CONTROLLER_NOS, CONTROLLER_Gear_Up, CONTROLLER_Gear_Down, CONTROLLER_Cruise_Control, CONTROLLER_Record_Movements_On
    global CONTROLLER_Record_Movements_On, CONTROLLER_Record_Movements_Off

    config.read(correctPath[0])

    #[DEVICE SETTINGS]
    MAC_ADDRESS                     = str(config.get('DEVICE_SETTINGS', 'MAC_ADDRESS'))
    BLUETOOTH_CHANNEL               = int(config.get('DEVICE_SETTINGS', 'BLUETOOTH_CHANNEL'))

    #[DRIVE_SETTINGS]
    Transmission                    = str(config.get('DRIVE_SETTINGS', 'Transmission'))

    #[KEYBOARD_MAPPING]
    KEYBOARD_Steer_Left             = config.get('KEYBOARD_MAPPING', 'Steer Left')
    KEYBOARD_Steer_Right            = config.get('KEYBOARD_MAPPING', 'Steer Right')
    KEYBOARD_Accelerate             = config.get('KEYBOARD_MAPPING', 'Accelerate')
    KEYBOARD_Break_Reverse          = config.get('KEYBOARD_MAPPING', 'Break/Reverse')
    KEYBOARD_Hand_Break             = config.get('KEYBOARD_MAPPING', 'Hand Break')
    KEYBOARD_NOS                    = config.get('KEYBOARD_MAPPING', 'N.O.S')
    KEYBOARD_Gear_Up                = config.get('KEYBOARD_MAPPING', 'Gear Up')
    KEYBOARD_Gear_Down              = config.get('KEYBOARD_MAPPING', 'Gear Down')
    KEYBOARD_Cruise_Control         = config.get('KEYBOARD_MAPPING', 'Cruise Control')
    KEYBOARD_Record_Movements_On    = config.get('KEYBOARD_MAPPING', 'Record Movements On')
    KEYBOARD_Record_Movements_Off   = config.get('KEYBOARD_MAPPING', 'Record Movements Off')

    #[CONTROLLER_MAPPING]
    CONTROLLER_Steer_Left             = config.get('CONTROLLER_MAPPING', 'Steer Left')
    CONTROLLER_Steer_Right            = config.get('CONTROLLER_MAPPING', 'Steer Right')
    CONTROLLER_Accelerate             = config.get('CONTROLLER_MAPPING', 'Accelerate')
    CONTROLLER_Break_Reverse          = config.get('CONTROLLER_MAPPING', 'Break/Reverse')
    CONTROLLER_Hand_Break             = config.get('CONTROLLER_MAPPING', 'Hand Break')
    CONTROLLER_NOS                    = config.get('CONTROLLER_MAPPING', 'N.O.S')
    CONTROLLER_Gear_Up                = config.get('CONTROLLER_MAPPING', 'Gear Up')
    CONTROLLER_Gear_Down              = config.get('CONTROLLER_MAPPING', 'Gear Down')
    CONTROLLER_Cruise_Control         = config.get('CONTROLLER_MAPPING', 'Cruise Control')
    CONTROLLER_Record_Movements_On    = config.get('CONTROLLER_MAPPING', 'Record Movements On')
    CONTROLLER_Record_Movements_Off   = config.get('CONTROLLER_MAPPING', 'Record Movements Off')

def print_entire_config():
    # [DEVICE SETTINGS]
    print (MAC_ADDRESS)
    print (BLUETOOTH_CHANNEL)

    # [DRIVE_SETTINGS]
    print (Transmission)

    # [print (KEYBOARD_MAPPING]
    print (KEYBOARD_Steer_Left)
    print (KEYBOARD_Steer_Right)
    print (KEYBOARD_Accelerate)
    print (KEYBOARD_Break_Reverse)
    print (KEYBOARD_Hand_Break)
    print (KEYBOARD_NOS)
    print (KEYBOARD_Gear_Up)
    print (KEYBOARD_Gear_Down)
    print (KEYBOARD_Cruise_Control)
    print (KEYBOARD_Record_Movements_On)
    print (KEYBOARD_Record_Movements_Off)

    # [print (CONTROLLER_MAPPING]
    print (CONTROLLER_Steer_Left)
    print (CONTROLLER_Steer_Right)
    print (CONTROLLER_Accelerate)
    print (CONTROLLER_Break_Reverse)
    print (CONTROLLER_Hand_Break)
    print (CONTROLLER_NOS)
    print (CONTROLLER_Gear_Up)
    print (CONTROLLER_Gear_Down)
    print (CONTROLLER_Cruise_Control)
    print (CONTROLLER_Record_Movements_On)
    print (CONTROLLER_Record_Movements_Off)


#TODO TESTING IF UPDATE CONFIG FIELD WORKS WITH CORRECTPATH[0]
def update_config_field(section, option, value):
    config.set(section, option, value)
    with open(correctPath[0], 'w') as configfile:
        config.write(configfile)
    load_config()




