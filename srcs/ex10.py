'''Define a function overlapping() that takes two lists and returns True if they
 have at least one member in common, False otherwise. You may use your
 is_member() function, or the in operator, but for the sake of the exercise,
 you should (also) write it using two nested for-loops.'''

def overlapping(lst1, lst2):
	'''
	This function returns true if two lists passed as parameters have a least one
	member in common

	Parameters
	----------
	lst1 (list)
	lst2 (list)

	Returns
	----------
	True the two lists shares at least one member in common
	False otherwise
	'''
	return max([i == j for j in lst2 for i in lst2])

def overlapping2(list1, list2):
	"""
	Same thing, without comprehensive list
	Use of nested loops
	"""

	for n in list1:
		for p in list2:
			if n == p:
				return True
	return False
