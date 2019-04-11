'''Write a function find_longest_word() that takes a list of words and returns
the length of the longest one.'''

from ex03 import length

def find_longest_word(lst):
  '''
  This function takes a list of words and returns the length of longest word

  Parameters
  ----------
  lst (list of strings)

  Returns
  ----------
  The length of the longest word (int)
  '''
  max = 0
  for n in [length(w) for w in lst]:
      if n > max:
          max = n
  return max

'''Uncomment the following lines to test the function and try to change the
the lists passed to the find_longest_word() function.'''

# lst1 = ['I', 'want', 'to', 'travel', 'to', 'Cambodia']
# lst2 = ['Python', 'is', 'cool']
# print('Length of longest word = {}'.format(find_longest_word(lst1)))
# print('Length of longest word = {}'.format(find_longest_word(lst2)))
