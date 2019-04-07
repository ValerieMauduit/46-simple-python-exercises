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


'''Uncomment the following lines to test the function and try to change the
list passed to the histogram() function.
'''

# print(histogram([4, 9, 7]))
# print(histogram([1, 2, 3, 4]))
