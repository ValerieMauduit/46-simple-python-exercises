import pytest, sys

sys.path = ['..', 'srcs']

from ex04 import is_vowel

def test_is_vowel_01():
  result = is_vowel('a')
  assert result == True

def test_is_vowel_02():
  result = is_vowel('b')
  assert result == False

def test_is_vowel_bad_type():
  with pytest.raises(TypeError) as e:
    is_vowel(42)
  assert str(e.value) == "object of type 'int' has no len()"

def test_is_vowel_bad_len():
  with pytest.raises(ValueError) as e:
    is_vowel('banana')
  assert str(e.value) == 'This function requires a character (string of size 1).'
