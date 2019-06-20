'''Define a function max_of_three() that takes three numbers as arguments
and returns the largest of them.'''

from srcs.ex01 import mymax

def max_of_three(n1, n2, n3):
  '''
  This function takes three numbers as arguments and returns the largest of them

	Parameters
	----------
	n1 (int or float): first number
	n2 (int or float): second number
	n3 (int or float): third number

	Returns
	----------
	The largest of the three numbers
	'''
	return mymax(mymax(n1, n2), n3)