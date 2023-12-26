def convert(hours, minutes):
	#solution for converting hours and minutes to seconds
	z=(3600*hours)+(60*minutes)
	return z
Test.assert_equals(convert(1, 0), 3600)
Test.assert_equals(convert(1, 3), 3780)
Test.assert_equals(convert(0, 30), 1800)