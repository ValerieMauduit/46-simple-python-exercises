import pytest, sys

sys.path = ['..', 'srcs']

from ex13 import max_in_list

def test_max_in_list_01():
  result = max_in_list([4, 9, 7, 12, 42, 5])
  assert result == 42

def test_max_in_list_02():
  result = max_in_list([10.8, 4.2, 7.8, 12.4, 6.8])
  assert result == 12.4

def test_max_in_list_bad_type():
  with pytest.raises(TypeError) as e:
    max_in_list('banana')
  assert str(e.value) == "'>' not supported between instances of 'str' and 'int'"
