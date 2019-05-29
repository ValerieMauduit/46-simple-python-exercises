'''Define a function max_of_three() that takes three numbers as arguments
and returns the largest of them.'''

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
	if n1 > n2 and n1 > n3:
		return n1
	elif n2 > n3:
		return n2
	else:
		return n3

