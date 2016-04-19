import bluetooth


##http://blog.kevindoran.co/bluetooth-programming-with-python-3/
#=============================================================================
# Global variables
# mac_address:  mac_address = mac address of the device that is going to be connected. (string)
# port_number:  port = port to be used with bluetooth - arbitrary number - should match server/client (integer)
# bt_socket:    socket with parameters for bluetooth connectivity (socket)
# =============================Global variables=================================
mac_address = ""
port_number = ""
bt_socket = ""
# =============================================================================
# Name:       set_device_settings(self, mac_address, port_number)
# Arguments:  mac_address = mac address of the device that is going to be connected.
# Purpose:    Initialises global variables mac_address,port_number,bt_socket
# ==============================================================================
def set_up_device(address, port):
    global mac_address
    global port_number
    mac_address = address
    port_number = port
# =============================================================================
# =============================================================================
# Name:       set_up_bluetooth_socket()
# Purpose:    Initialises bt_socket as bluetooth socket
# ==============================================================================
def set_up_bluetooth_socket():
    global bt_socket
    bt_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# =============================================================================
# =============================================================================
# Name:       connect_bluetooth()
# Purpose:    Attempts to connect to the bluetooth device with mac address and port number
#             or exists with error messages of what went wrong.
# ==============================================================================
def connect_bluetooth():
    try:
        bt_socket.connect((mac_address, port_number))
        print("Successful connection was established with {0}:".format(
            mac_address))
    except Exception as e:
        raise SystemExit("Something went wrong while connecting to {0}, Exception is {1}:".format(
            mac_address, e)+"\nExiting program now.!")
# =============================================================================
# =============================================================================
# Name:       send_command(self, command_value)
# Arguments:  command_value = a hex code that will be understandable to bluetooth car
# Purpose:    Sends data to the bluetooth car
# ==============================================================================
def send_command(command_value):
    print("Sending command Now!")
    bt_socket.send(command_value)
# =============================================================================
# =============================================================================
# Name:       disconnect_bluetooth(self)
# Purpose:    closes connection over socket.
# ==============================================================================
def disconnect_bluetooth():
    bt_socket.close()
    print("Closing bluetooth socket now!")
# =============================================================================
# =============================================================================




# ==================================TESTING====================================


# =============================================================================
# Name:       get_global_variables(mac_address, port_number)
# Arguments:  mac_address = mac address of the device that is going to be set
# Arguments:  port = port that is going to be set
# Purpose:    returns set values for mac and port
# ==============================================================================
def get_global_variables(address, port):
    set_up_device(address, port)
    return mac_address, port_number