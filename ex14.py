'''Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words.'''

from ex03 import length

def words_to_len(lst):
  '''
  This function takes a list of words and returns their lengths

  Parameters
  ----------
  lst (list of strings)

  Returns
  ----------
  A list of integers
  '''
  return [length(w) for w in lst]


'''The expected program below:'''

def main():
    lst1 = ['I', 'want', 'to', 'sleep']
    lst2 = words_to_len(lst1)

    return print(lst2)

if __name__ == '__main__':
    main()
