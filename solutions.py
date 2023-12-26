
def convert(hours, minutes):
	"""
	https://edabit.com/challenge/PjcKZRx8YE5KzRN63
	solution for converting hours and minutes to seconds
	"""
	z=(3600*hours)+(60*minutes)
	return z

def addition(a, b):
	"""
	addition of two numbers
	https://edabit.com/challenge/rZToTkR5eB9Zn4zLh
	"""
	return a+b

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
		return num1+num2
	elif operator == "-":
		return num1-num2
	elif operator == "*":
		return num1*num2
	elif operator == "/":
		return num1/num2