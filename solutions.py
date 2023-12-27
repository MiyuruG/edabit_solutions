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

def animals(chickens, cows, pigs)
"""https://edabit.com/challenge/QzXtDnSZL6y4ZcEvT
Right the first time!"""
	return (2*chickens)+(4*cows)+(4*pigs)