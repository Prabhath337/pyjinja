#class basicmath contains basic algebric functions, where it takes a,b as input and return the output.

class maths():

# html is a class variable and an dictionary object.
	html={}
	P='Pass'
	F='Fail'

# addition is a function with two input variables a,b
	def addition(self,a,b):
		try:
			return a+b
		except ArithmeticError as ex:
			print(ex)

# substraction is a function with two input variables a,b
	def substraction(self,a,b):
		try:
			return a-b
		except ArithmeticError as ex:
			print(ex)

# multiplication is a function with two input variables a,b
	def multiplication(self,a,b):
		try:
			return a*b
		except ArithmeticError as ex:
			print(ex)

# division is a function with two input variables a,b
	def division(self,a,b):
		try:
			return a/b
		except ZeroDivisionError:
			print("Please enter valid number as one cannot divide by zero")

if __name__=="__main__":
	algeb=maths()
	alsub=algeb.substraction(1,-10.000)
	print(alsub)

