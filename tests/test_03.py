import pytest, sys

sys.path = ['..', 'srcs']

from ex03 import length

def test_length_01():
  result = length('Hello world!')
  assert result == 12

def test_length_02():
  result = length([0, 1, 2, 3, 4, 5])
  assert result == 6
