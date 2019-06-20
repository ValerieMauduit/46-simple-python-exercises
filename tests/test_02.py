import pytest, sys

sys.path = ['..', 'srcs']

from ex02 import max_of_three

def test_max_of_three_01():
  result = max_of_three(2, 6, 42)
  assert result == 42

def test_max_of_three_02():
  result = max_of_three(10.8, 5.4, 0.1)
  assert result == 10.8

def test_max_of_three_03():
  result = max_of_three(100, 1000, 4000)
  assert result == 4000
