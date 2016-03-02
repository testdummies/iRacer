import socket
import time


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:

    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:

    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


class BluetoothCar:

    def __init__(self, mac_address="00:12:05:11:97:90"):

        # def __init__(self, mac_address="00:12:05:09:97:76"):
        self.socket = socket.socket(
            socket.AF_BLUETOOTH,
            socket.SOCK_STREAM,
            socket.BTPROTO_RFCOMM)

        self.socket.connect((mac_address, 1))

    def drive(self, duration):
        print "sending command now"
        self.socket.send('\x18')
        time.sleep(duration)

car = BluetoothCar()
getch = _Getch()
#car = BluetoothCar()
while True:
    c = getch.impl()
    if c == "w":
        print 'input' + str(c)
    else:
        print 'input' + str(c)
        #car.drive(0.01)
