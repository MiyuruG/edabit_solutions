import unittest
from solutions import convert, calculator

class Test_Solutions(unittest.TestCase):
    def test_convert_hours_and_minutes_to_seconds(self):
        self.assertEquals(convert(1, 0), 3600)
        self.assertEquals(convert(1, 3), 3780)
        self.assertEquals(convert(0, 30), 1800)
"""
Test.assert_equals(addition(2,3), 5)
Test.assert_equals(addition(-3,-6), -9)
Test.assert_equals(addition(7,3), 10)

Test.assert_equals(bool_to_string(True), "True")
Test.assert_equals(bool_to_string(False), "False")


Test.assert_equals(calculator(2, '/', 2), 1)
Test.assert_equals(calculator(10, '-', 7), 3)
Test.assert_equals(calculator(2, '*', 16), 32)
Test.assert_equals(calculator(2, '-', 2), 0)
Test.assert_equals(calculator(15, '+', 26), 41)
Test.assert_equals(calculator(2, '+', 2), 4)
Test.assert_equals(calculator(2, "/", 0), "Can't divide by 0!")

"""