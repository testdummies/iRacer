#!/usr/bin/env python

# About:
# Project:          Raspberry PI to control Bluetooth car.
# Team Name:        'Test Dummies'
# Authors:          Amadi Chimenem,
#                   Gall Martyn,
#                   Goszka Krzysztof,
#                   Jackson John,
#                   Walker Ross.
# Program Name:     iRacer_controls:
# Description:      Python based controls for iRacer car over bluetooth.
# License:          No licence - Open project - CHANGE THAT OFFICIAL LICENCE
# Revision:         see git rev. - ADD GIT
#---------------------------------------------------------------------

# Suggestions:
# These are just suggestions:
# 1. Limit lines to 70 characters- PEP-8 limits it to 79.
# 2. Indent using tabs that are set to 4 spaces(in text editor).
# 3. Use some inline comments.
# 4. Start to handle error cases.
# 5. Change hard-coded constants to program parameters.
#---------------------------------------------------------------------

# Import required libraries.
import sys

# Program parameters.
#
# Control Bytes are Constructed in Hex like this:
# 0xXY - Where X is the direction and Y is the speed.
# By using most significant bit for direction and least significant bit for speed,
# hexadecimal addition can be performed to receive hex value that will correspond
# to both direction and speed as single byte in 0xXY format.
#
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

Direction = dict()
Direction [0    ] = 0x00
Direction [1    ] = 0x10
Direction [2    ] = 0x20
Direction [3    ] = 0x30
Direction [4    ] = 0x40
Direction [5    ] = 0x50
Direction [6    ] = 0x60
Direction [7    ] = 0x70
Direction [8    ] = 0x80

Speed = dict()
Speed [0        ] = 0x00
Speed [1        ] = 0x01
Speed [2        ] = 0x02
Speed [3        ] = 0x03
Speed [4        ] = 0x04
Speed [5        ] = 0x05
Speed [6        ] = 0x06
Speed [7        ] = 0x07
Speed [8        ] = 0x08
Speed [9        ] = 0x09
Speed [10       ] = 0x0A
Speed [11       ] = 0x0B
Speed [12       ] = 0x0C
Speed [13       ] = 0x0D
Speed [14       ] = 0x0E
Speed [15       ] = 0x0F

#METHODS
#DO NOT CHANGE METHODS THAT WERE TESTED.
#---------------------------------------------------------------------

#TESTED METHODS BELOW:
# Name:       speed_to_Hex(inputValue):
# Arguments:  inputValue is a decimal value.
# Purpose:    Looks up hexadecimal value using decimal input as a key
# Example:    inputValue = 10, return = 0x0A
def speed_to_Hex(inputValue):
    return Speed[inputValue]
#---------------------------------------------------------------------
#---------------------------------------------------------------------

# Name:       direction_to_Hex(inputValue):
# Arguments:  inputValue is a decimal value.
# Purpose:    Looks up hexadecimal value using decimal input as a key
# Example:    inputValue = 3, return = 0x30
def direction_to_Hex(inputValue):
    return Direction[inputValue]
#---------------------------------------------------------------------
#---------------------------------------------------------------------

# Name:       combineInput(Direction,Speed)
# Arguments:  Direction = Hex value for Direction
#             Speed = Hex value for Speed
# Purpose:    Combines both Direction and Speed into single byte.
# Example:    Direction = 0x30, Speed = 0x09, return = 0x39.
def combineInput(Direction,Speed):
    return direction_to_Hex(Direction) + speed_to_Hex(Speed)
#---------------------------------------------------------------------

#Need to figure this part out and apply logic from other examples
def readSpeed:
    #input from keyboard or xbox controller... or anything

def readDirection:
    #input from keyboard or xbox controller... or anything
def readInput:
    #input from keyboard or xbox controller... or anything
    readSpeed
    readDirection


#TESTING BIT - TESTING ONLY BELOW THE LINE:
#_____________________________________________________________________________#



print format(direction_to_Hex(7), '02x')
print format(speed_to_Hex(11), '02x')
print format(combineInput(7,11), '02x')
