'''Write a function is_member() that takes a value (i.e. a number, string, etc)
x and a list of values a, and returns True if x is a member of a,
False otherwise.
(Note that this is exactly what the in operator does, but for the sake of the
exercise you should pretend Python did not have this operator.)'''

def is_member(x, a):
	'''
	This function checks if a value x is a member of a list of values a

	Parameters
	----------
	x (string, int, float): a value
	a (list): a list of values

	Returns
	----------
	True if x is in the list a
	False otherwise
	'''
	return x in a
