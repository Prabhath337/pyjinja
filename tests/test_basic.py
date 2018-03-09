import basicmath
#import pytest


# setup_method method runs everytime before test method.
math=basicmath.maths()

# test_addition method asserts whether a passed arguments or inputs meets the expected value

def test_addition():
	testname="Verify whether addition of two numbers working as expected"
	expected=1
	actual=math.addition(3,7)
	print(actual)
	try:
		assert actual==expected
		print("Passed")
		return [testname,expected,actual,math.P]
	except:
		print("Failed")
		return [testname,expected,actual,math.F]

# test_substraction method asserts whether a passed arguments or inputs meets the expected value

def test_substraction():
	testname="Verify whether substraction of two numbers working as expected"
	expected=-4
	actual=math.substraction(3,7)
	try:
		assert actual==expected
		return [testname,expected,actual,math.P]
	except:
		return [testname,expected,actual,math.F]

def teardown_function():
	try:
		math.html[test_addition()[0]]=test_addition()
		math.html[test_substraction()[0]]=test_substraction()
	except Exception as ex:
		print(ex)
