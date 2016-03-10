import socket
import sys

mac_address = ""
port_numbe = 0
pin_number = ""

socket = socket.socket(
    socket.AF_BLUETOOTH,
    socket.SOCK_STREAM,
    socket.BTPROTO_RFCOMM)


def device_settings(mac_addr, port_num, pin_num):
    global mac_address, port_number, pin_number
    mac_address = mac_addr
    port_number = port_num
    pin_number = pin_num


def pair_Bluetooth():
    print "pairing with PIN goes here"


def connect_Bluetooth():
    try:
        socket.connect((mac_address, port_number))
        print("Successful connection was established with {0}:".format(
            mac_address))
    except Exception as e:
        print("Something went wrong while connecting to {0}, Exception is {1}:".format(
            mac_address, e))
        print "Exiting program now"
        sys.exit()


def send_command(command_value):
    print "Sending command Now!"
    socket.send(command_value)
