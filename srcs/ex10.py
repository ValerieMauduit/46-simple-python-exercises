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
  if [i == j for j in lst2 for i in lst1 if i == j]:
    return True
  return False
