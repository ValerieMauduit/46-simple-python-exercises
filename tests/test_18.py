import pytest, sys

sys.path = ['..', 'srcs']

from ex18 import is_pangram

def test_is_pangram_01():
  result = is_pangram("The quick brown fox jumps over the lazy dog")
  assert result == True

def test_is_pangram_02():
  result = is_pangram("You are searching for a random sentence")
  assert result == False

def test_is_pangram_bad_type():
  with pytest.raises(TypeError) as e:
    is_pangram(42)
  assert str(e.value) == "'int' object is not iterable"
