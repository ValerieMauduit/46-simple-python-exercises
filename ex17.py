'''Write a version of a palindrome recognizer that also accepts phrase
palindromes such as "Go hang a salami I'm a lasagna hog.",
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization,
and spacing are usually ignored.'''

def is_phrase_palindrome(str):
  '''
  This function recognizes palindromes and accepts phrase palindromes
  (i.e. words that look the same written backwards)
  Punctuation, capitalization, and spacing are usually ignored

  Parameters
  ----------
  str (string)

  Returns
  ----------
  True if the phrase is a palindrome
  False otherwise
  '''
  phrase = [i.lower() for i in str if i.isalpha()]
  return phrase == phrase[::-1]

'''Uncomment the following lines to test the function and try to change the
string passed to the is_phrase_palindrome() function.'''

# print(is_phrase_palindrome("Go hang a salami I'm a lasagna hog."))
# print(is_phrase_palindrome("Was it a rat I saw?"))
# print(is_phrase_palindrome("Dammit, I'm mad!"))
# print(is_phrase_palindrome("Where are the students?"))
# print(is_phrase_palindrome("Let's go to the movie theater!"))
