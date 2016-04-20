import unittest
import modules.bluetooth_controls.connection as bt_connection

if __name__ == '__main__':
    unittest.main()

class Test_connection(unittest.TestCase):

    # ============Testing global_variables=============#
    def test_set_up_device(self):
        self.assertEquals(("test",1),bt_connection.get_global_variables("test", 1))

##ADD MORE TESTS IF POSSIBLE