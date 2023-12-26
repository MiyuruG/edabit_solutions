import unittest
from solutions import convert

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


"""