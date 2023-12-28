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

Test.assert_equals(animals(5, 2, 8), 50)
Test.assert_equals(animals(3, 4, 7), 50)
Test.assert_equals(animals(1, 2, 3), 22)
Test.assert_equals(animals(3, 5, 2), 34)

Test.assert_equals(squared(10), 100, "Expected 100")
Test.assert_equals(squared(69), 4761, "Expected 4761")
Test.assert_equals(squared(666), 443556, "Expected 443556")
Test.assert_equals(squared(-21), 441, "Expected 441")
Test.assert_equals(squared(21), 441, "Expected 441")

Test.assert_equals(football_points(1, 2, 3), 5)
Test.assert_equals(football_points(5, 5, 5), 20)
Test.assert_equals(football_points(1, 0, 0), 3)
Test.assert_equals(football_points(0, 7, 0), 7)
Test.assert_equals(football_points(0, 0, 15), 0)

Test.assert_equals(cubes(2), 8)
Test.assert_equals(cubes(3), 27)
Test.assert_equals(cubes(4), 64)
Test.assert_equals(cubes(5), 125)
Test.assert_equals(cubes(10), 1000)

Test.assert_equals(less_than_or_equal_to_zero(5), False)
Test.assert_equals(less_than_or_equal_to_zero(0), True)
Test.assert_equals(less_than_or_equal_to_zero(-5), True)

Test.assert_equals(points(1, 1),5)
Test.assert_equals(points(1, 2), 8)
Test.assert_equals(points(2, 1), 7)
Test.assert_equals(points(2, 2), 10)
Test.assert_equals(points(69, 420), 1398)

#Made by c h a e r (11level360) 
#              <3


Test.assert_equals(makes10(9, 10), True)	
Test.assert_equals(makes10(9, 9), False)	
Test.assert_equals(makes10(1, 9), True)	
Test.assert_equals(makes10(10, 1), True)	
Test.assert_equals(makes10(10, 10), True)	
Test.assert_equals(makes10(8, 2), True)	
Test.assert_equals(makes10(8, 3), False)	
Test.assert_equals(makes10(10, 42), True)	
Test.assert_equals(makes10(12, -2), True)

Test.assert_equals(less_than_100(5, 57), True)
Test.assert_equals(less_than_100(77, 30), False)
Test.assert_equals(less_than_100(0, 59), True)
Test.assert_equals(less_than_100(78, 35), False)
Test.assert_equals(less_than_100(63, 11), True)
Test.assert_equals(less_than_100(37, 99), False)
Test.assert_equals(less_than_100(52, 11), True)
Test.assert_equals(less_than_100(82, 95), False)
Test.assert_equals(less_than_100(17, 44), True)
Test.assert_equals(less_than_100(74, 53), False)
Test.assert_equals(less_than_100(3, 77), True)
Test.assert_equals(less_than_100(25, 80), False)
Test.assert_equals(less_than_100(59, 28), True)
Test.assert_equals(less_than_100(69, 87), False)
Test.assert_equals(less_than_100(10, 45), True)
Test.assert_equals(less_than_100(43, 58), False)
Test.assert_equals(less_than_100(50, 44), True)
Test.assert_equals(less_than_100(74, 89), False)
Test.assert_equals(less_than_100(3, 27), True)
Test.assert_equals(less_than_100(21, 79), False)


Test.assert_equals(circuit_power(110, 3), 330)
Test.assert_equals(circuit_power(230, 10), 2300)
Test.assert_equals(circuit_power(480, 20), 9600)

Test.assert_equals(is_same_num(4, 8), False)
Test.assert_equals(is_same_num(2, 2), True)
Test.assert_equals(is_same_num(0, 6), False)
Test.assert_equals(is_same_num(2, "2"), False)

# Originally created by @Vladislav Kobylnyk
"""