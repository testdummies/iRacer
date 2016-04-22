import time
import modules.bluetooth_controls.connection as bt
import modules.interface.keyboard_input as key
import modules.configuration.active_settings as settings



def check_pressed_keys_settings():
    settings.load_config()
    bt.initialise_bluetooth_settings()
    time.sleep(2)
    bt.connect_bluetooth()
    time.sleep(2)
    key.check_active_keys()


#check_pressed_keys_settings()
