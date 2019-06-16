import pytest, sys

sys.path = ['..', 'srcs']

from ex17 import is_phrase_palindrome

def test_is_phrase_palindrome_01():
  result = is_phrase_palindrome("Go hang a salami I'm a lasagna hog.")
  assert result == True

def test_is_phrase_palindrome_02():
  result = is_phrase_palindrome("Dammit, I'm mad!")
  assert result == True

def test_is_phrase_palindrome_03():
  result = is_phrase_palindrome("Where are the students?")
  assert result == False

def test_is_phrase_palindrome_bad_type():
  with pytest.raises(TypeError) as e:
    is_phrase_palindrome(42)
  assert str(e.value) == "'int' object is not iterable"
