import pytest, sys

sys.path = ['..', 'srcs']

from ex01 import mymax

def test_mymax_01():
  result = mymax(2, 8)
  assert result == 8

def test_mymax_02():
  result = mymax(6.8, 0.3)
  assert result == 6.8
