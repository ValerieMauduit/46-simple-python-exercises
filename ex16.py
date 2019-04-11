'''Write a function filter_long_words() that takes a list of words and
an integer n and returns the list of words that are longer than n.'''

from ex03 import length

def filter_long_words(lst, n):
  '''
  This function filters a list of words and returns them if longer than n

  Parameters
  ----------
  lst (list of strings)
  n (int)

  Returns
  ----------
  The list of words that are longer than n (list of strings)
  '''
  return [w for w in lst if length(w) > n]

'''Uncomment the following lines to test the function and try to change the
the list and the length passed to the filter_long_words() function.'''

# lst1 = ['I', 'want', 'to', 'travel', 'to', 'Cambodia']
# lst2 = ['Python', 'is', 'cool']
# print(filter_long_words(lst1, 2))
# print(filter_long_words(lst1, 5))
# print(filter_long_words(lst2, 3))
# print(filter_long_words(lst2, 8))
