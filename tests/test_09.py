import pytest, sys

sys.path = ['..', 'srcs']

from ex09 import is_member

def test_is_member_01():
  result = is_member('a', [0, 1, 2, 3, 4, 5])
  assert result == False

def test_is_member_02():
  result = is_member(1, [0, 1, 2, 3, 4, 5])
  assert result == True

def test_is_member_03():
  result = is_member('hello', ['hello', 'world'])
  assert result == True
