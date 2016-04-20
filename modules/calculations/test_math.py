import unittest
import modules.calculations.math as math

if __name__ == '__main__':
    unittest.main()

class Test_math(unittest.TestCase):

    # ============Testing int to hex and hex to int=============#
    def test_int_to_hex_to_int(self):
        hex1= math.int_to_hex(10)
        #integer to hex
        hex2 = math.int_to_hex(math.hex_to_int(math.int_to_hex(10)))
        #int to hex,hex to int and int to hex again
        self.assertEquals(hex1, hex2)

        hex1= math.int_to_hex(19)
        #integer to hex
        hex2 = math.int_to_hex(math.hex_to_int(math.int_to_hex(19)))
        #int to hex,hex to int and int to hex again
        self.assertEquals(hex1, hex2)


    # ============Testing get_direction_value(current_direction)=============#
    def test_get_direction_value(self):
        self.assertEquals(0, math.get_direction_value("STOP"))
        self.assertEquals(16, math.get_direction_value("FS"))
        self.assertEquals(32, math.get_direction_value("RS"))
        self.assertEquals(48, math.get_direction_value("NL"))
        self.assertEquals(64, math.get_direction_value("NR"))
        self.assertEquals(80, math.get_direction_value("FL"))
        self.assertEquals(96, math.get_direction_value("FR"))
        self.assertEquals(112, math.get_direction_value("RL"))
        self.assertEquals(128, math.get_direction_value("RR"))


    # ============Testing get_speed_value(current_gear)=============#
    def test_get_speed_value(self):
        self.assertEquals(6, math.get_speed_value(-1))
        self.assertEquals(6, math.get_speed_value(1))
        self.assertEquals(7, math.get_speed_value(2))
        self.assertEquals(8, math.get_speed_value(3))
        self.assertEquals(9, math.get_speed_value(4))
        self.assertEquals(10, math.get_speed_value(5))
        self.assertEquals(11, math.get_speed_value(6))
        self.assertEquals(12, math.get_speed_value(7))
        self.assertEquals(13, math.get_speed_value(8))
        self.assertEquals(14, math.get_speed_value(9))
        self.assertEquals(15, math.get_speed_value(10))

    # ============Testing get_combined_value(current_direction, current_gear)=============#
    def test_get_combined_value(self):
        combined_hex = math.get_combined_value("FS", 6)
        combined_int = math.hex_to_int(combined_hex)
        expected_code = 27
        self.assertEquals(expected_code, combined_int)

        combined_hex = math.get_combined_value("STOP", 0)
        combined_int = math.hex_to_int(combined_hex)
        expected_code = 0
        self.assertEquals(expected_code, combined_int)

        combined_hex = math.get_combined_value("NL", 0)
        combined_int = math.hex_to_int(combined_hex)
        expected_code = 48
        self.assertEquals(expected_code, combined_int)

        combined_hex = math.get_combined_value("RR", 10)
        combined_int = math.hex_to_int(combined_hex)
        expected_code = 143
        self.assertEquals(expected_code, combined_int)