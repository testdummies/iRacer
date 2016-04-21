import bluetooth
import time
import modules.configuration.active_settings as st

# =============================================================================
# Global variables
# mac_address:  mac_address = mac address of the device that is going to be connected. (string)
# port_number:  port = port to be used with bluetooth_controls - arbitrary number - should match server/client (integer)
# bt_socket:    socket with parameters for bluetooth_controls connectivity (socket)
# =============================Global variables=================================
mac_address = "1"
port_number = "1"
bt_socket = "1"


# =============================================================================
# Name:       initialise_bluetooth_settings()
# Purpose:    Initialises bt_socket as bluetooth_controls socket and mac address and port
# ==============================================================================
def initialise_bluetooth_settings():
    global mac_address
    global port_number
    global bt_socket

    print ("\n")
    st.load_config()
    print ("loading config file")
    mac_address = st.MAC_ADDRESS
    print ("Setting up mac address as: " + mac_address)
    port_number = st.BLUETOOTH_CHANNEL
    print ("Setting up port as: " + str(port_number))
    bt_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    print ("Setting up bluetooth socket")
# =============================================================================


# =============================================================================
# Name:       connect_bluetooth()
# Purpose:    Attempts to connect to the bluetooth_controls device with mac address and port number
#             or exists with error messages of what went wrong.
# ==============================================================================
def connect_bluetooth():
    print ("\n")
    try:
        bt_socket.connect((mac_address, port_number))
        print("Successful connection was established with {0}:".format(
            mac_address))
    except Exception as e:
        raise SystemExit("Something went wrong while connecting to {0}, Exception is {1}:".format(
            mac_address, e) + "\nExiting program now.!")


# =============================================================================


# =============================================================================
# Name:       send_command(command_value, time_delay)
# Arguments:  command_value = a hex code that will be understandable to bluetooth_controls car
# Arguments:  time_delay = time required to wait
# Purpose:    Sends data to the bluetooth_controls car
# ==============================================================================
def send_command(command_value, time_delay):
    #print("Sending command Now!")
    bt_socket.send(command_value)
    time.sleep(time_delay)


# =============================================================================


# =============================================================================
# Name:       disconnect_bluetooth(self)
# Purpose:    closes connection over bluetooth socket.
# ==============================================================================
def disconnect_bluetooth():
    bt_socket.close()
    print("Closing bluetooth_controls socket now!")


# =============================================================================
# =============================================================================

