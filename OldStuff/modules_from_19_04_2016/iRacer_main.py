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

from OldStuff.modules_from_19_04_2016 import iRacer_input


def bluetooth_connect():
    mac_address = "00:12:05:11:97:90"
    port_number = 1
    pin_number = "1234"
    #connect car - bluetooth#
    iRacer_bluetooth.device_settings(mac_address, port_number, pin_number)
    iRacer_bluetooth.connect_Bluetooth()


bluetooth_connect()
iRacer_input.start_keyboard_input()
