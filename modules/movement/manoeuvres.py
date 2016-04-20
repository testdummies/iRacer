import modules.calculations.math as math
import modules.bluetooth_controls.connection as bt


# TODO CHECK IF GEAR 1 which is 1 lower than speed 2 is working correctly.
# Speed will always be 2 due to using time to maneuver
# Increasing speed will throw off out calibrates movements
# Speed 2 also allows to show movements and get more consistent traction
# Maneuvers will not be perfect as car has limitations

# Three point turn to right hand side using 3 main movements,
# Should end up facing 180 degrees on opposite side of the "Road"


# =============================================================================
# Name:       execute_manoeuvre(time_list, gear_list, direction_list)
# Arguments:  time_list = list with times in sequence for time sleep
# Arguments:  gear_list = list with gears in sequence for changing gears
# Arguments:  direction_list = list with directions in sequence for changing direction
# Purpose:    Unified method that will be called by each manoeuvre method
# ==============================================================================
def execute_manoeuvre(time_list, gear_list, direction_list):
    for i in range(len(time_list)):
        command = math.get_combined_value(direction_list[i], gear_list[i])
        bt.send_command(command, time_list[i])


# =============================================================================
# Name:         three_point_turn_right()
# Description:  TODO description
# ==============================================================================
def three_point_turn_right():
    sq_time = [2, 2.4, 1, 1.6, 1, 1.48]
    sq_gear = [1, 1, 1, 1, 1, 1]
    sq_direction = ["STOP", "FR", "STOP", "RL", "STOP", "FR"]
    execute_manoeuvre(sq_time, sq_gear, sq_direction)


# =============================================================================
# Name:         three_point_turn_left()
# Description:  Three point turn to left hand side using 3 main movements,
#                Should end up facing 180 degrees on oposite side of the "Road"
# ==============================================================================
def three_point_turn_left():
    sq_time = [2, 2, 1, 2, 1, 1.4]
    sq_gear = [1, 1, 1, 1, 1, 1]
    sq_direction = ["STOP", "FL", "STOP", "RR", "STOP", "FL"]
    execute_manoeuvre(sq_time, sq_gear, sq_direction)


# =============================================================================
# Name:         parallel_parking_right_side()
# Description:  Parallel park to right hand side using 3 turning movements to achieve it
# ==============================================================================
def parallel_parking_right_side():
    # Combined all settings to sequence lists
    sq_time = [2, 1.3, 1, 1.1, 1, 0.6, 1, 0.3]  # sequence time etc.
    sq_gear = [1, 1, 1, 1, 1, 1, 1, 1]
    sq_direction = ["STOP", "RR", "STOP", "RL", "STOP", "FR", "STOP", "FS"]
    execute_manoeuvre(sq_time, sq_gear, sq_direction)


# =============================================================================
# Name:         parallel_parking_left_side()
# Description:  parallel park to left hand side using 3 turning movements to achieve it
# ==============================================================================
def parallel_parking_left_side():
    sq_time = [2, 1.3, 1, 0.8, 1, 0.8, 1, 0.1]
    sq_gear = [1, 1, 1, 1, 1, 1, 1, 1]
    sq_direction = ["STOP", "RL", "STOP", "RR", "STOP", "FL", "STOP", "FS"]
    execute_manoeuvre(sq_time, sq_gear, sq_direction)


# =============================================================================
# Name:         turn_around_left()
# Description:  180 turn going to left with 1 long movement
# ==============================================================================
def turn_around_left():
    sq_time = [2, 5]
    sq_gear = [1, 1]
    sq_direction = ["STOP", "FL"]
    execute_manoeuvre(sq_time, sq_gear, sq_direction)


# =============================================================================
# Name:         turn_around_right()
# Description:  180 turn going to right with 1 long movement
# ==============================================================================
def turn_around_right():
    sq_time = [2, 5]
    sq_gear = [1, 1]
    sq_direction = ["STOP", "FR"]
    execute_manoeuvre(sq_time, sq_gear, sq_direction)


# =============================================================================
# Name:         circle_right()
# Description:  360 turn going to right with 1 long movement
# ==============================================================================
def circle_right():
    sq_time = [2, 9]
    sq_gear = [1, 1]
    sq_direction = ["STOP", "FR"]
    execute_manoeuvre(sq_time, sq_gear, sq_direction)


# =============================================================================
# Name:         circle_left()
# Description:  360 turn going to left with 1 long movement
# ==============================================================================
def circle_left():
    sq_time = [2, 9]
    sq_gear = [1, 1]
    sq_direction = ["STOP", "FL"]
    execute_manoeuvre(sq_time, sq_gear, sq_direction)
