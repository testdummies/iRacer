import struct

debugging = False


# =============================================================================
# Name:       int_to_hex(int_value)
# Arguments:  int_value = integer value
# Purpose:    Converts integer to hexadecimal byte in '\x00' format
# Example:    int_value = 0 converted = '\x00'
# =============================================================================
def int_to_hex(int_value):
    converted = struct.pack('1B', int_value)
    if debugging:
        print ("\n")
        print ("Method: int_to_hex(" + str(int_value) + "):")
        print ("converted: " + str(converted))
    return converted
# =============================================================================


# =============================================================================
# Name:       hex_to_int(hex_value)
# Arguments:  hex_value = A string of hex value formatted in '\x50' format
# Purpose:    converts a hex value to integer that corresponds to that value
# Example:    hex_value = '\x00' converted[0] = 0
# ==============================================================================
def hex_to_int(hex_value):
    converted = struct.unpack('1B', hex_value)
    if debugging:
        print ("\n")
        print ("Method: hex_to_int(" + str(hex_value) + "):")
        print ("converted: " + str(converted))
        print ("converted[0]: " + str(converted[0]))
    return converted[0]
# ==============================================================================


# =============================================================================
# Name:       get_direction_value(current_direction)
# Arguments:  current_direction = a string describing current direction
# Purpose:    returns a decimal number corresponding to direction required
# =============================================================================
def get_direction_value(current_direction):

    direction = dict()
    direction["STOP"] = 0   # Stop                  - '\x00'

    direction["FS"] = 16    # Forward Straight      - '\x10'
    direction["RS"] = 32    # Reverse Straight      - '\x20'

    direction["NL"] = 48    # Neutral Left          - '\x30'
    direction["NR"] = 64    # Neutral Right         - '\x40'

    direction["FL"] = 80    # Forward Left          - '\x50'
    direction["FR"] = 96    # Forward Right         - '\x60'

    direction["RL"] = 112   # Reverse Left          - '\x70'
    direction["RR"] = 128   # Reverse Right         - '\x80'

    return direction[current_direction]


# =============================================================================
# Name:       get_speed_value(current_gear)
# Arguments:  current_gear = an int describing current gear
# Purpose:    returns a decimal number corresponding to speed required
# =============================================================================
def get_speed_value(current_gear):

    speed = dict()
    speed[-1] = 6   # slowest reliable speed reverse     - '\x00'

    speed[0] = 0    # no gear / stopped  - '\x00'

    speed[1] = 7  # first gear         - '\x07'
    speed[2] = 8  # second gear        - '\x08'
    speed[3] = 9  # third gear         - '\x09'
    speed[4] = 10  # fourth gear        - '\x0A'
    speed[5] = 11  # fifth gear        - '\x0B'
    speed[6] = 12  # sixth gear        - '\x0C'
    speed[7] = 13  # seventh gear      - '\x0D'
    speed[8] = 14  # eighth gear       - '\x0E'
    speed[9] = 15  # ninth gear        - '\x0F'
    return speed[current_gear]

'''
    speed[1] = 6    # first gear         - '\x06'
    speed[2] = 7    # second gear        - '\x07'
    speed[3] = 8    # third gear         - '\x08'
    speed[4] = 9    # fourth gear        - '\x09'
    speed[5] = 10    # fifth gear        - '\x0A'
    speed[6] = 11    # sixth gear        - '\x0B'
    speed[7] = 12    # seventh gear      - '\x0C'
    speed[8] = 13    # eighth gear       - '\x0D'
    speed[9] = 14    # ninth gear        - '\x0E'
    speed[10] = 15    # tenth gear       - '\x0F'
    '''


# =============================================================================
# Name:       get_combined_value(current_direction, current_gear)
# Arguments:  current_direction = a string describing current direction
# Arguments:  current_gear = an int describing current gear
# Purpose:    returns a hexadecimal number corresponding to direction and speed
# =============================================================================
def get_combined_value(current_direction, current_gear):
    direction_value = get_direction_value(current_direction)
    speed_value = get_speed_value(current_gear)
    #print direction_value
    #print speed_value

    return int_to_hex(direction_value+speed_value)
