import pytest, sys

sys.path = ['..', 'srcs']

from ex08 import is_palindrome

def test_is_palindrome_01():
  result = is_palindrome('radar')
  assert result == True

def test_is_palindrome_02():
  result = is_palindrome('hello')
  assert result == False

def test_is_palindrome_bad_type():
  with pytest.raises(TypeError) as e:
    is_palindrome(42)
  assert str(e.value) == "'int' object is not subscriptable"
