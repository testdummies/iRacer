import time
import modules.bluetooth.connection as bt_connection


bt_connection.set_up_device("00:12:05:11:97:90",1)
bt_connection.set_up_bluetooth_socket()
bt_connection.connect_bluetooth()
bt_connection.send_command('\x80')
time.sleep(2)
bt_connection.disconnect_bluetooth()