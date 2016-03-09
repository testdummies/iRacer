import sys
import select
import tty
import termios
import socket
#import bluetooth
import time
from evdev import InputDevice, categorize, ecodes
import struct

if __name__ == '__main__':

    dev = InputDevice('/dev/input/event3')

    #bd_addr = "00:12:05:11:97:90"
    bd_addr = "00:12:05:11:97:909"
    port = 1
    #sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)


    sock = socket.socket(
        socket.AF_BLUETOOTH,
        socket.SOCK_STREAM,
        socket.BTPROTO_RFCOMM)

def initconnection():
    try:
        sock.connect((bd_addr, 1))
        print 'Connected'
    except:
        print 'Socket error, could not connect to device'
        sys.exit()

def add_hex2(x, y):
    tupleX = struct.unpack('1B',x)
    tupleY = struct.unpack('1B',y)

    tmp = tupleX[0] + tupleY[0]
    command = struct.pack('1B',tmp)
    return command


def command_send(command,duration):
    sock.send(command)
    time.sleep(duration)
    sock.send('\x00')

initconnection()
command = add_hex2('\x20','\x06')
command_send(command,1)

#    for event in dev.read_loop():
#
#        if event.type == ecodes.EV_KEY:
#            key_pressed = str(categorize(event))
#            if 'KEY_LEFT' in key_pressed:
#        # 0x5X for left forward. 0x51 very slow. 0x5F fastest
#                sock.send('\x5A')
#            if 'KEY_RIGHT' in key_pressed:
#        # 0x6X for right forward. 0x11 very slow. 0x1F fastest
#                sock.send('\x6A')
#            if 'KEY_DOWN' in key_pressed:
#        # 0x2X for straight backward. 0x21 very slow. 0x2F fastest
#                sock.send('\x2A')
#            if 'KEY_UP' in key_pressed:
#        # 0x1X for straight forward. 0x11 very slow. 0x1F fastest
#                sock.send('\x1A')
#            if 'KEY_SPACE' in key_pressed:
#        # stop
##                sock.send('\x00')
#            if 'KEY_1' in key_pressed:
#                sock.send('\x1A')
