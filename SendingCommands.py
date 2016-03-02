import socket
import time

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

if __name__ == "__main__":
    car = BluetoothCar()
    # if the connection succeeds then we can run car commands
    if car.connectToBluetooth():
        while True:
            car.drive(0.05)
    # otherwise we say not connected
    else:
        print 'not connected'
