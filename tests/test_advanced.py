# !usr/bin/python

import pytest
import basicmath

# setup_method method runs everytime before test method.
math=basicmath.maths()

# test_addition method asserts whether a passed arguments or inputs meets the expected value

def test_multiplication():
	testname="Verify whether multiplication of two numbers working as expected"
	expected=21
	actual=math.multiplication(3,7)
	try:
		assert actual==expected
		return [testname,expected,actual,math.P]
	except:
		return [testname,expected,actual,math.F]

# test_division method asserts whether a passed arguments or inputs meets the expected value

def test_division():
	testname="Verify whether division of two numbers working as expected"
	expected=-4
	actual=math.division(3,7)
	try:
		assert actual==expected
		return [testname,expected,actual,math.P]
	except:
		return [testname,expected,actual,math.F]

def teardown_function():
	try:
		math.html[test_division()[0]]=test_division()
		math.html[test_multiplication()[0]]=test_multiplication()
	except Exception as ex:
		print(ex)
