# About:
# Project:          Raspberry PI to control Bluetooth car.
# Team Name:        'Test Dummies'
# Authors:          Amadi Chimenem,
#                   Gall Martyn,
#                   Goszka Krzysztof,
#                   Jackson John,
#                   Walker Ross.
# Program Name:     iRacer_main:
# Description:      Python based controls for iRacer car over bluetooth.
# License:          No licence - Open project - CHANGE THAT OFFICIAL LICENCE
# Revision:         see git rev. - ADD GIT
#---------------------------------------------------------------------
import iRacer_bluetooth
import iRacer_controls

mac_address = "00:12:05:11:97:90"
port_number = 1
pin_number = "1234"
#connect car - bluetooth#
iRacer_bluetooth.device_settings(mac_address, port_number, pin_number)
iRacer_bluetooth.connect_Bluetooth()

#send commands#
#dir_hex = '\x10'
#speed_hex = '\x05'
time = 5

direction = iRacer_controls.direction_lookup("Dir_SF")
speed = iRacer_controls.speed_lookup(4)

value = iRacer_controls.combine_inputs(direction, speed)
iRacer_controls.car_drive(value, time)
