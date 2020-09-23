# Author: Mark Mendez
# Date: 9/23/2020
# Description: test file for multiply_three_numbers.py

import unittest
from multiply_three_numbers import multiply_3

class TestMult3(unittest.TestCase):
    """contains unit tests for the multiply_3() function"""
    def test_positive_ints(self):
        number1 = 2
        number2 = 3
        number3 = 4
        result = multiply_3(number1, number2, number3)
        self.assertEqual(result, 24)

    def test_floats(self):
        number1 = 2.2
        number2 = 3.3
        number3 = 4.4
        result = multiply_3(number1, number2, number3)
        self.assertAlmostEqual(result, 31.9440, 2)  # test accuracy to 2 places

    def test_int_float_mixed(self):
        number1 = 2
        number2 = 3.3
        number3 = 4.4
        result = multiply_3(number1, number2, number3)
        self.assertAlmostEqual(result, 29.0400, 2)  # test accuracy to 2 places

    def test_zero_int_float(self):
        number1 = 2
        number2 = 0
        number3 = 4.4
        result = multiply_3(number1, number2, number3)
        self.assertEqual(result, 0)

    def test_negative_int_float_mixed(self):
        number1 = -2
        number2 = 3.3
        number3 = 4.4
        result = multiply_3(number1, number2, number3)
        self.assertAlmostEqual(result, -29.0400, 2)  # test accuracy to 2 places

    def test_all_negative_floats(self):
        number1 = -2
        number2 = -3.3
        number3 = -4.4
        result = multiply_3(number1, number2, number3)
        self.assertAlmostEqual(result, -29.0400, 2)  # test accuracy to 2 places

if __name__ == '__main__':
    unittest.main()