import pytest, sys

sys.path = ['..', 'srcs']

from ex12 import histogram

def test_histogram_01():
  result = histogram([4, 9, 7])
  hist = '''****\n*********\n*******'''
  assert result == hist

def test_histogram_02():
  result = histogram([1, 2, 3, 4])
  hist = '''*\n**\n***\n****'''
  assert result == hist

def test_histogram_bad_type():
  with pytest.raises(TypeError) as e:
    histogram('banana')
  assert str(e.value) == "can't multiply sequence by non-int of type 'str'"
