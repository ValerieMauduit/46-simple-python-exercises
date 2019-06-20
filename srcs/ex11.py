'''Define a function generate_n_chars() that takes an integer n and a character
c and returns a string, n characters long, consisting only of c:s.
For example, generate_n_chars(5,"x") should return the string "xxxxx".
(Python is unusual in that you can actually write an expression 5 * "x" that
will evaluate to "xxxxx". '''

def generate_n_chars(n, c):
  '''
  This function generates n times the c character

  Parameters
  ----------
  n (int): a number
  c (string of length 1): a character

  Returns
  ----------
  A string of n characters long, consisting only of c
  '''
  return n * c
