'''The function max() from exercise 1) and the function max_of_three() from
exercise 2) will only work for two and three numbers, respectively. But suppose
we have a much larger number of numbers, or suppose we cannot tell in advance
how many they are? Write a function max_in_list() that takes a list of numbers
and returns the largest one.'''

def max_in_list(lst):
	'''
	This function takes a list of numbers and returns the largest one

	Parameters
	----------
	lst (list of integers or floats)

	Returns
	----------
	The largest of the numbers
	'''
	max = 0
	for n in lst:
		if n > max:
			max = n
	return max
