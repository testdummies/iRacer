import sys
import socket
import time
from evdev import InputDevice, categorize, ecodes

class BluetoothCar:
    def connectToBluetooth(self):
        mac_address="00:12:05:11:97:90"
        connect = False

        self.socket = socket.socket(
            socket.AF_BLUETOOTH,
            socket.SOCK_STREAM,
            socket.BTPROTO_RFCOMM)

        try:
            # test the connection to the car and catch any errors
            # if the connection succeeds then we return a bool
            self.socket.connect((mac_address, 1))
            print 'connected to car'
            connect = True
        except Exception as e:
            # display the error and return false to say connection failed
            print("something's wrong with {0}, Exception is {1}:".format(mac_address, e))
            connect = False

        return connect

    def drive(self,duration):
        self.socket.send('\x16')
        time.sleep(duration)

if __name__ == '__main__':
    car = BluetoothCar()
    dev = InputDevice('/dev/input/event3')
    
    # if the connection succeeds then we can run car commands
    if car.connectToBluetooth():
        while True:
            for event in dev.read_loop():
              if event.type == ecodes.EV_KEY:
                  key_pressed = str(categorize(event))
                  if 'KEY_LEFT' in key_pressed:
                      # 0x5X for left forward. 0x51 very slow. 0x5F fastest
                      car.send('\x5A')
                  if 'KEY_RIGHT' in key_pressed:
                      # 0x6X for right forward. 0x11 very slow. 0x1F fastest
                      sock.send('\x6A')
                  if 'KEY_DOWN' in key_pressed:
                       # 0x2X for straight backward. 0x21 very slow. 0x2F fastest
                      sock.send('\x2A')
                  if 'KEY_UP' in key_pressed:
                       # 0x1X for straight forward. 0x11 very slow. 0x1F fastest
                      sock.send('\x1A')
                  if 'KEY_SPACE' in key_pressed:
                      # stop
                      sock.send('\x00')
    # otherwise we say not connected
    else:
        print 'not connected'

    
