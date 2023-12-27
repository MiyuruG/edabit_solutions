import unittest
from solutions import convert, calculator, sum_odd_and_even, list_of_multiples

class Test_Solutions(unittest.TestCase):
    def test_convert_hours_and_minutes_to_seconds(self):
        self.assertEqual(convert(1, 0), 3600)
        self.assertEqual(convert(1, 3), 3780)
        self.assertEqual(convert(0, 30), 1800)
    
    def test_sum_odd_and_even(self):
        self.assertEqual(sum_odd_and_even([1, 2, 3, 4, 5, 6]), [12, 9])
        self.assertEqual(sum_odd_and_even([-1, -2, -3, -4, -5, -6]), [-12, -9])
        self.assertEqual(sum_odd_and_even([0, 0]), [0, 0])
        self.assertEqual(sum_odd_and_even([]), [0, 0])

    def test_list_of_multiples(self):
        self.assertEqual(list_of_multiples(7, 5),[7, 14, 21, 28, 35])
        self.assertEqual(list_of_multiples(12, 10), [12, 24, 36, 48, 60, 72, 84, 96, 108, 120])
        self.assertEqual(list_of_multiples(17, 7), [17, 34, 51, 68, 85, 102, 119])
        self.assertEqual(list_of_multiples(630, 14), [630, 1260, 1890, 2520, 3150, 3780, 4410, 5040, 5670, 6300, 6930, 7560, 8190, 8820])
        self.assertEqual(list_of_multiples(140, 3), [140, 280, 420])
        self.assertEqual(list_of_multiples(7, 8), [7, 14, 21, 28, 35, 42, 49, 56])
        self.assertEqual(list_of_multiples(11, 21), [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231])
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

Test.assert_equals(sum_odd_and_even([1, 2, 3, 4, 5, 6]), [12, 9])
Test.assert_equals(sum_odd_and_even([-1, -2, -3, -4, -5, -6]), [-12, -9])
Test.assert_equals(sum_odd_and_even([0, 0]), [0, 0])
Test.assert_equals(sum_odd_and_even([]), [0, 0])


Test.assert_equals(hello(), "hello edabit.com")

"""