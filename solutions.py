def convert(hours, minutes):
    """
	https://edabit.com/challenge/PjcKZRx8YE5KzRN63
	solution for converting hours and minutes to seconds
	"""
    return (3600 * hours) + (60 * minutes)


def addition(a, b):
    """
	addition of two numbers
	https://edabit.com/challenge/rZToTkR5eB9Zn4zLh
	"""
    return a + b


def bool_to_string(flag):
    """
	https://edabit.com/challenge/QQp2o22huzBCkHesy
	converting boolean to string
	"""
    if flag:
        return "True"
    return "False"


def calculator(num1, operator, num2):
    """
	https://edabit.com/challenge/ZdnwC3PsXPQTdTiKf
	calculator to deal with two numbers
	"""
    if num2 == 0 and operator == '/':
        return "Can't divide by 0!"

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2


def sum_odd_and_even(lst):
    """
	https://edabit.com/challenge/5XXXppAdfcGaootD9
	Return a list of odd and even sums
	"""
    odd_sum = 0
    even_sum = 0

    for element in lst:
        if (element % 2) == 0:
            even_sum = even_sum + element
        else:
            odd_sum = odd_sum + element

    osnda_lst = [even_sum, odd_sum]
    return osnda_lst


def list_of_multiples(num, length):
    """
    https://edabit.com/challenge/BuwHwPvt92yw574zB
    TODO: Miyuru will add more description
    """
    return_list = list()
    x = 0
    while True:
        x = x + 1
        return_list.append(x * num)
        if length <= x:
            break
    return return_list


def hello():
    """https://edabit.com/challenge/8ym3dKrL3svkYr4h4
        the easiest one
    """
    return "hello edabit.com"


def animals(chickens, cows, pigs):
    """https://edabit.com/challenge/QzXtDnSZL6y4ZcEvT
    Right the first time!"""
    return (2 * chickens) + (4 * cows) + (4 * pigs)


def squared(b):
    """https://edabit.com/challenge/sLkTkfLgZYs5wejsg"""
    return b * b


def football_points(wins, draws, losses):
    """no google/chat gpt https://edabit.com/challenge/gwqqc5p3oiFXRJAQm"""
    return (3 * wins) + (1 * draws) + (0 * losses)


def cubes(a):
    """https://edabit.com/challenge/CjXamaNRmKxwkmBxq no google/chat gpt"""
    return a ** 3


def less_than_or_equal_to_zero(num):
    """https://edabit.com/challenge/Rx2pkSA9dCmtwS8xt
    i only use w3 school!"""
    return (num <= 0)


def points(twopointers, threepointers):
    """https://edabit.com/challenge/KWnJrMzK9CumnfxTF
    no google/chat gpt"""
    return (2 * twopointers) + (3 * threepointers)


def makes10(a, b):
    """https://edabit.com/challenge/HuWQaCpFR7iTeCvTm
    When the time box was over, I asked the chat gpt.
    """
    return a == 10 or b == 10 or a + b == 10


def less_than_100(a, b):
    """https://edabit.com/challenge/pZ3HxBfvejsvkEDo4
    no google/chat gpt
    Done in 3 minutes!"""
    return a + b < 100


def circuit_power(voltage, current):
    """https://edabit.com/challenge/v5gc8FQkDEepkqpfp
    no google/chat gpt
    Done in 1 minute"""
    return voltage * current


def is_same_num(num1, num2):
    """https: // edabit.com / challenge / yfooETHj3sHoHTJsv
    no google/chat gpt"""
    return num1 == num2

import math

def circle_or_square(radius, area):
    # Calculate the circumference of the circle
    circumference = 2 * math.pi * radius

    # Calculate the side length of the square from its area
    side_length = math.sqrt(area)

    # Calculate the perimeter of the square
    square_perimeter = 4 * side_length

    # Compare the circumference of the circle and the perimeter of the square
    return circumference > square_perimeter


def circle_or_square(radius, area):
    """https://edabit.com/challenge/4me7LifXBwj5rhL4n this cord from Chat GPT.But i can't undestand the code"""
    # Calculate the circumference of the circle
    circumference = 2 * math.pi * radius

    # Calculate the side length of the square from its area
    side_length = math.sqrt(area)

    # Calculate the perimeter of the square
    square_perimeter = 4 * side_length
    # Compare the circumference of the circle and the perimeter of the square
    return circumference > square_perimeter



