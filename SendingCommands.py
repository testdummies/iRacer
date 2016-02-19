import socket
import time

class BluetoothCar:
    #def __init__(self, mac_address="00:12:05:11:97:90"):
    def __init__(self, mac_address="00:12:05:09:97:76"):
        self.socket = socket.socket(
            socket.AF_BLUETOOTH,
            socket.SOCK_STREAM,
            socket.BTPROTO_RFCOMM)

        self.socket.connect((mac_address, 1))

    def drive(self,duration):
        print "sending command now"
        self.socket.send('\x55')
        time.sleep(duration)

if __name__ == "__main__":
    car = BluetoothCar()
    while True:
        car.drive(0.05)

#F works
#E
#
