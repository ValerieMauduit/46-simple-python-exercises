import pytest, sys

sys.path = ['..', 'srcs']

from ex23 import correct

def test_correct_01():
  result = correct('This   is  very funny  and    cool.Indeed!')
  assert result == 'This is very funny and cool. Indeed!'

def test_correct_bad_type():
  with pytest.raises(TypeError) as e:
    correct(42)
  assert str(e.value) == "expected string or bytes-like object"
