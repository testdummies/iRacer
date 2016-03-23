import iRacer_controls
 
#Controls to put variables in to data that the car can take in using other modules
def controls(direction,speed,time):
    look_direction = iRacer_controls.direction_lookup(direction)
    look_speed = iRacer_controls.speed_lookup(speed)
 
    value = iRacer_controls.combine_inputs(look_direction, look_speed)
    iRacer_controls.car_drive(value, time)
 
#@@@@@@@@@@@@@@@@@@@@@@@INFORMATION@@@@@@@@@@@@@@@@@@@@
#Speed will always be 2 due to using time to maneuver
#Increasing speed will throw off out calibrates movements
#Speed 2 also allows to show movements and get more consistant traction
#Maneuvers will not be perfect as car has limitations
 
#Three point turn to right hand side using 3 main movements,
#Should end up facing 180 degrees on oposite side of the "Road"
def three_point_turn_right():
 
    #Combined all settings to sequence lists
    sq_time = [2,2.4,1,1.6,1,1.48] #sequence time etc.
    sq_speed = [2,2,2,2,2,2]
    sq_direction = ["Dir_Stop","Dir_RF","Dir_Stop","Dir_LB","Dir_Stop","Dir_RF"]
    #for each item in sequence, call method with corresponding values
    for i in range(len(sq_time)):
        controls(sq_direction[i],sq_speed[i],sq_time[i])
 
#Three point turn to left hand side using 3 main movements,
#Should end up facing 180 degrees on oposite side of the "Road"
def three_point_turn_left():
 
    #Combined all settings to sequence lists
    sq_time = [2,2,1,2,1,1.4] #sequence time etc.
    sq_speed = [2,2,2,2,2,2]
    sq_direction = ["Dir_Stop","Dir_LF","Dir_Stop","Dir_RB","Dir_Stop","Dir_LF"]
    #for each item in sequence, call method with corresponding values
    for i in range(len(sq_time)):
        controls(sq_direction[i],sq_speed[i],sq_time[i])
 
 
#Parallel park to right hand side using 3 turning movements to achieve it
def parralel_parking_right_side():
 
    #Combined all settings to sequence lists
    sq_time = [2,1.3,1,1.1,1,0.6,1,0.3] #sequence time etc.
    sq_speed = [2,2,2,2,2,2,2,2]
    sq_direction = ["Dir_Stop","Dir_RB","Dir_Stop","Dir_LB","Dir_Stop","Dir_RF","Dir_Stop","Dir_SF"]
    #for each item in sequence, call method with corresponding values
    for i in range(len(sq_time)):
        controls(sq_direction[i],sq_speed[i],sq_time[i])
 
 
#Parallel park to left hand side using 3 turning movements to achieve it
def parralel_parking_left_side():
 
    #Combined all settings to sequence lists
    sq_time = [2,1.3,1,0.8,1,0.8,1,0.1] #sequence time etc.
    sq_speed = [2,2,2,2,2,2,2,2]
    sq_direction = ["Dir_Stop","Dir_LB","Dir_Stop","Dir_RB","Dir_Stop","Dir_LF","Dir_Stop","Dir_SF"]
    #for each item in sequence, call method with corresponding values
    for i in range(len(sq_time)):
        controls(sq_direction[i],sq_speed[i],sq_time[i])
 
#180 turn going to left with 1 long movement
def turn_around_left():
 
    #Combined all settings to sequence lists
    sq_time = [2,5] #sequence time etc.
    sq_speed = [2,2]
    sq_direction = ["Dir_Stop","Dir_LF"]
    #for each item in sequence, call method with corresponding values
    for i in range(len(sq_time)):
        controls(sq_direction[i],sq_speed[i],sq_time[i])
 
#180 turn going to right with 1 long movement
def turn_around_right():
 
    #Combined all settings to sequence lists
    sq_time = [2,5] #sequence time etc.
    sq_speed = [2,2]
    sq_direction = ["Dir_Stop","Dir_RF"]
    #for each item in sequence, call method with corresponding values
    for i in range(len(sq_time)):
        controls(sq_direction[i],sq_speed[i],sq_time[i])
 
#360 turn going to right with 1 long movement
def circle_right():
 
    #Combined all settings to sequence lists
    sq_time = [2,9] #sequence time etc.
    sq_speed = [2,2]
    sq_direction = ["Dir_Stop","Dir_RF"]
    #for each item in sequence, call method with corresponding values
    for i in range(len(sq_time)):
        controls(sq_direction[i],sq_speed[i],sq_time[i])
 
#360 turn going to left with 1 long movement
def circle_left():
 
    #Combined all settings to sequence lists
    sq_time = [2,9] #sequence time etc.
    sq_speed = [2,2]
    sq_direction = ["Dir_Stop","Dir_LF"]
    #for each item in sequence, call method with corresponding values
    for i in range(len(sq_time)):
        controls(sq_direction[i],sq_speed[i],sq_time[i])
