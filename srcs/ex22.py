'''In cryptography, a Caesar cipher is a very simple encryption techniques in
which each letter in the plain text is replaced by a letter some fixed number of
positions down the alphabet. For example, with a shift of 3, A would be replaced
by D, B would become E, and so on. The method is named after Julius Caesar,
who used it to communicate with his generals. ROT-13 ("rotate by 13 places")
is a widely used example of a Caesar cipher where the shift is 13. In Python,
the key for ROT-13 may be represented by means of the following dictionary:

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

Your task in this exercise is to implement an encoder/decoder of ROT-13.
Once you're done, you will be able to read the following secret message:

   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!

Note that since English has 26 characters, your ROT-13 program will be able to
both encode and decode texts written in English.'''

import string

def merge_dicts(d1, d2):
  '''
  This function takes two dictionaries and merges them

  Parameters
  ----------
  d1 (dict)
  d2 (dict)

  Returns
  ----------
  The merged dictionary
  '''
  d = d1.copy()
  d.update(d2)
  return d

def create_key(n):
  '''
  This function rotates the alphabet by n places

  Parameters
  ----------
  n (int)

  Returns
  ----------
  A dictionary
  '''
  lower_lst = list(string.ascii_lowercase)
  lower_lst2 = lower_lst[n:] + lower_lst[:n]
  upper_lst = list(string.ascii_uppercase)
  upper_lst2 = upper_lst[n:] + upper_lst[:n]

  d1 = dict(zip(lower_lst, lower_lst2))
  d2 = dict(zip(upper_lst, upper_lst2))

  return merge_dicts(d1, d2)


def rot13(str):
  '''
  This function takes a string and encodes or decodes it following the
  Caesar cipher technique

  Parameters
  ----------
  str (string)

  Returns
  ----------
  The converted string
  '''
  key = create_key(13)
  return ''.join([key[c] if c in key else c for c in str])
