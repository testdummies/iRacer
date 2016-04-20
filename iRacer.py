import time
import modules.bluetooth_controls.connection as bt_connection
import modules.movement.manoeuvres as mv


bt_connection.set_up_device("00:12:05:11:97:90",1)
bt_connection.set_up_bluetooth_socket()
bt_connection.connect_bluetooth()
mv.parallel_parking_left_side()
#bt_connection.send_command('\x80')
#time.sleep(2)
bt_connection.disconnect_bluetooth()