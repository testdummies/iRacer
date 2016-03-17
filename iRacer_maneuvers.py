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

    #Give the stop signal to try and sync the bluetooth before sending
    #the actual movement commands to try and make it more consistant
    time = 2
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes right forward for 2.4 seconds at speed 2
    time = 2.4
    speed = 2
    direction = "Dir_RF"
    controls(direction,speed,time)

    #Stops for one second after last command (seems to increase consistancy)
    time = 1
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes left back for 1.6 seconds
    time = 1.6
    speed = 2
    direction = "Dir_LB"
    controls(direction,speed,time)

    #Stops for one second after last command (seems to increase consistancy)
    time = 1
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes right forward for 1.48 seconds
    time = 1.48
    speed = 2
    direction = "Dir_RF"
    controls(direction,speed,time)

#Three point turn to left hand side using 3 main movements,
#Should end up facing 180 degrees on oposite side of the "Road"
def three_point_turn_left():

    #Give the stop signal to try and sync the bluetooth before sending
    #the actual movement commands to try and make it more consistant
    time = 2
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes left forward for 2 seconds
    time = 2
    speed = 2
    direction = "Dir_LF"
    controls(direction,speed,time)

    #Stops for one second after last command (seems to increase consistancy)
    time = 1
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes right back for 2 seconds
    time = 2
    speed = 2
    direction = "Dir_RB"
    controls(direction,speed,time)

    #Stops for one second after last command (seems to increase consistancy)
    time = 1
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes left forward for 1.4 seconds
    time = 1.4
    speed = 2
    direction = "Dir_LF"
    controls(direction,speed,time)

#Parallel park to right hand side using 3 turning movements to achieve it
def parralel_parking_right_side():

    #Give the stop signal to try and sync the bluetooth before sending
    #the actual movement commands to try and make it more consistant
    time = 2
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes right back for 1.3 seconds
    time = 1.3
    speed = 2
    direction = "Dir_RB"
    controls(direction,speed,time)

    #Stops for one second after last command (seems to increase consistancy)
    time = 1
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes left back for 1.1 seconds
    time = 1.1
    speed = 2
    direction = "Dir_LB"
    controls(direction,speed,time)

    #Stops for one second after last command (seems to increase consistancy)
    time = 1
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes right forward for 0.6 seconds
    time = 0.6
    speed = 2
    direction = "Dir_RF"
    controls(direction,speed,time)

    #Stops for one second after last command (seems to increase consistancy)
    time = 1
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes Straight forward for 0.3 seconds (just to get closer to a real parallel park)
    time = 0.3
    speed = 2
    direction = "Dir_SF"
    controls(direction,speed,time)

#Parallel park to left hand side using 3 turning movements to achieve it
def parralel_parking_left_side():

    #Give the stop signal to try and sync the bluetooth before sending
    #the actual movement commands to try and make it more consistant
    time = 2
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes left back for 1.5 seconds
    time = 1.5
    speed = 2
    direction = "Dir_LB"
    controls(direction,speed,time)

    #Stops for one second after last command (seems to increase consistancy)
    time = 1
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes right back for 1 second
    time = 1
    speed = 2
    direction = "Dir_RB"
    controls(direction,speed,time)

    #Stops for one second after last command (seems to increase consistancy)
    time = 1
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes left forward for 0.7 seconds
    time = 0.7
    speed = 2
    direction = "Dir_LF"
    controls(direction,speed,time)

    #Stops for one second after last command (seems to increase consistancy)
    time = 1
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Goes Straight forward for 0.3 seconds (just to get closer to a real parallel park)
    time = 0.3
    speed = 2
    direction = "Dir_SF"
    controls(direction,speed,time)

#180 turn going to left with 1 long movement
def turn_around_left():

    #Give the stop signal to try and sync the bluetooth before sending
    #the actual movement commands to try and make it more consistant
    time = 2
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Go left forward 5.5 seconds till facing 180 degreess
    time = 5.5
    speed = 2
    direction = "Dir_LF"
    controls(direction,speed,time)

#180 turn going to right with 1 long movement
def turn_around_right():

    #Give the stop signal to try and sync the bluetooth before sending
    #the actual movement commands to try and make it more consistant
    time = 2
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Go right forward for 5 seconds till facing 180 degrees
    time = 5
    speed = 2
    direction = "Dir_RF"
    controls(direction,speed,time)

#360 turn going to right with 1 long movement
def circle_right():

    #Give the stop signal to try and sync the bluetooth before sending
    #the actual movement commands to try and make it more consistant
    time = 2
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Go right forward for 10 seconds till facing 360 degrees
    time = 10
    speed = 2
    direction = "Dir_RF"
    controls(direction,speed,time)

#360 turn going to left with 1 long movement
def circle_left():

    #Give the stop signal to try and sync the bluetooth before sending
    #the actual movement commands to try and make it more consistant
    time = 2
    speed = 2
    direction = "Dir_Stop"
    controls(direction,speed,time)

    #Go left forward for 10 seconds till facing 360 degrees
    time = 11
    speed = 2
    direction = "Dir_LF"
    controls(direction,speed,time)
