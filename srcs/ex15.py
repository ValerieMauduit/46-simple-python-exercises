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
