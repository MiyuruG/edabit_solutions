import unittest

from solutions import convert, sum_odd_and_even, list_of_multiples, addition, bool_to_string, calculator, animals, \
    hello, squared, football_points, cubes, makes10, points, less_than_or_equal_to_zero, less_than_100, circuit_power, \
    is_same_num


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
        self.assertEqual(list_of_multiples(7, 5), [7, 14, 21, 28, 35])
        self.assertEqual(list_of_multiples(12, 10), [12, 24, 36, 48, 60, 72, 84, 96, 108, 120])
        self.assertEqual(list_of_multiples(17, 7), [17, 34, 51, 68, 85, 102, 119])
        self.assertEqual(list_of_multiples(630, 14),
                         [630, 1260, 1890, 2520, 3150, 3780, 4410, 5040, 5670, 6300, 6930, 7560, 8190, 8820])
        self.assertEqual(list_of_multiples(140, 3), [140, 280, 420])
        self.assertEqual(list_of_multiples(7, 8), [7, 14, 21, 28, 35, 42, 49, 56])
        self.assertEqual(list_of_multiples(11, 21),
                         [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220,
                          231])

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-3, -6), -9)
        self.assertEqual(addition(7, 3), 10)
        
    def test_bool_to_string(self):
        self.assertEqual(bool_to_string(True), "True")
        self.assertEqual(bool_to_string(False), "False")
    
    def test_calculator(self):
        self.assertEqual(calculator(2, '/', 2), 1)
        self.assertEqual(calculator(10, '-', 7), 3)
        self.assertEqual(calculator(2, '*', 16), 32)
        self.assertEqual(calculator(2, '-', 2), 0)
        self.assertEqual(calculator(15, '+', 26), 41)
        self.assertEqual(calculator(2, '+', 2), 4)
        self.assertEqual(calculator(2, "/", 0), "Can't divide by 0!")
    
    def test_sum_odd_and_even(self):
        self.assertEqual(sum_odd_and_even([1, 2, 3, 4, 5, 6]), [12, 9])
        self.assertEqual(sum_odd_and_even([-1, -2, -3, -4, -5, -6]), [-12, -9])
        self.assertEqual(sum_odd_and_even([0, 0]), [0, 0])
        self.assertEqual(sum_odd_and_even([]), [0, 0])
    
    def test_hello(self):
        self.assertEqual(hello(), "hello edabit.com")
    
    def test_animals(self):
        self.assertEqual(animals(5, 2, 8), 50)
        self.assertEqual(animals(3, 4, 7), 50)
        self.assertEqual(animals(1, 2, 3), 22)
        self.assertEqual(animals(3, 5, 2), 34)

    def test_squared(self):
        self.assertEqual(squared(10), 100, "Expected 100")
        self.assertEqual(squared(69), 4761, "Expected 4761")
        self.assertEqual(squared(666), 443556, "Expected 443556")
        self.assertEqual(squared(-21), 441, "Expected 441")
        self.assertEqual(squared(21), 441, "Expected 441")

    def test_football_points(self):
        self.assertEqual(football_points(1, 2, 3), 5)
        self.assertEqual(football_points(5, 5, 5), 20)
        self.assertEqual(football_points(1, 0, 0), 3)
        self.assertEqual(football_points(0, 7, 0), 7)
        self.assertEqual(football_points(0, 0, 15), 0)

    def test_cubes(self):
        self.assertEqual(cubes(2), 8)
        self.assertEqual(cubes(3), 27)
        self.assertEqual(cubes(4), 64)
        self.assertEqual(cubes(5), 125)
        self.assertEqual(cubes(10), 1000)

    def test_less_than_or_equal_to_zero(self):
        self.assertEqual(less_than_or_equal_to_zero(5), False)
        self.assertEqual(less_than_or_equal_to_zero(0), True)
        self.assertEqual(less_than_or_equal_to_zero(-5), True)

    def test_points(self):
        self.assertEqual(points(1, 1), 5)
        self.assertEqual(points(1, 2), 8)
        self.assertEqual(points(2, 1), 7)
        self.assertEqual(points(2, 2), 10)
        self.assertEqual(points(69, 420), 1398)

    def test_makes10(self):
        self.assertEqual(makes10(9, 10), True)
        self.assertEqual(makes10(9, 9), False)
        self.assertEqual(makes10(1, 9), True)
        self.assertEqual(makes10(10, 1), True)
        self.assertEqual(makes10(10, 10), True)
        self.assertEqual(makes10(8, 2), True)
        self.assertEqual(makes10(8, 3), False)
        self.assertEqual(makes10(10, 42), True)
        self.assertEqual(makes10(12, -2), True)

    def test_less_than_100(self):
        self.assertEqual(less_than_100(5, 57), True)
        self.assertEqual(less_than_100(77, 30), False)
        self.assertEqual(less_than_100(0, 59), True)
        self.assertEqual(less_than_100(78, 35), False)
        self.assertEqual(less_than_100(63, 11), True)
        self.assertEqual(less_than_100(37, 99), False)
        self.assertEqual(less_than_100(52, 11), True)
        self.assertEqual(less_than_100(82, 95), False)
        self.assertEqual(less_than_100(17, 44), True)
        self.assertEqual(less_than_100(74, 53), False)
        self.assertEqual(less_than_100(3, 77), True)
        self.assertEqual(less_than_100(25, 80), False)
        self.assertEqual(less_than_100(59, 28), True)
        self.assertEqual(less_than_100(69, 87), False)
        self.assertEqual(less_than_100(10, 45), True)
        self.assertEqual(less_than_100(43, 58), False)
        self.assertEqual(less_than_100(50, 44), True)
        self.assertEqual(less_than_100(74, 89), False)
        self.assertEqual(less_than_100(3, 27), True)
        self.assertEqual(less_than_100(21, 79), False)


    def test_circuit_power(self):
        self.assertEqual(circuit_power(110, 3), 330)
        self.assertEqual(circuit_power(230, 10), 2300)
        self.assertEqual(circuit_power(480, 20), 9600)
        
    def test_is_same_num(self):
        self.assertEqual(is_same_num(4, 8), False)
        self.assertEqual(is_same_num(2, 2), True)
        self.assertEqual(is_same_num(0, 6), False)
        self.assertEqual(is_same_num(2, "2"), False)
