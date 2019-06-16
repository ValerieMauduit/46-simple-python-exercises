'''A pangram is a sentence that contains all the letters of the English alphabet
at least once, for example: "The quick brown fox jumps over the lazy dog".
Your task here is to write a function to check a sentence to see if it is
a pangram or not.'''


def is_pangram(str):
  '''
  This function recognizes pangrams
  (i.e. a sentence that contains all the letters of the English alphabet
  at least once)

  Parameters
  ----------
  str (string)

  Returns
  ----------
  True if the sentence is a pangram
  False otherwise
  '''
  phrase = [i.lower() for i in str if i.isalpha()]
  clean = set(phrase)
  return len(clean) == 26
