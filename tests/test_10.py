import pytest, sys

sys.path = ['..', 'srcs']

from ex10 import overlapping

lst1 = [0, 1, 2, 3, 4, 5]
lst2 = ['hello world', 42]
lst3 = [4, 2, 42, 4.2]

def test_overlapping_01():
  result = overlapping(lst1, lst2)
  assert result == False

def test_overlapping_02():
  result = overlapping(lst1, lst3)
  assert result == True

def test_overlapping_03():
  result = overlapping(lst2, lst3)
  assert result == True
