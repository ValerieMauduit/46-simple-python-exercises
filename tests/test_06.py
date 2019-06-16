import pytest, sys

sys.path = ['..', 'srcs']

from ex06 import mysum, multiply

def test_sum():
  result = mysum([1, 2, 3, 4])
  assert result == 10

def test_multiply():
  result = (multiply([1, 2, 3, 4]))
  assert result == 24

def test_bad_type_sum():
  with pytest.raises(TypeError) as e:
    mysum('banana')
  assert str(e.value) == "unsupported operand type(s) for +=: 'int' and 'str'"

def test_bad_type_multiply():
  with pytest.raises(TypeError) as e:
    multiply('banana')
  assert str(e.value) == "can't multiply sequence by non-int of type 'str'"
