'''Define a procedure histogram() that takes a list of integers and prints a
histogram to the screen. For example, histogram([4, 9, 7])
should print the following:

****
*********
*******'''

def histogram(lst):
  '''
  This function takes prints a histogram to the screen based on a given list of
  integers

  Parameters
  ----------
  lst (list of integers)

  Returns
  ----------
  Prints a histogram
  '''
  for i in lst:
      print(i * '*')
  return None
