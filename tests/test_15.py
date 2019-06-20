import pytest, sys

sys.path = ['..', 'srcs']

from ex15 import find_longest_word

def test_find_longest_word_01():
  result = find_longest_word(['I', 'want', 'to', 'travel', 'to', 'Cambodia'])
  assert result == 8

def test_find_longest_word_02():
  result = find_longest_word(['Python', 'is', 'cool'])
  assert result == 6

def test_find_longest_word_bad_type():
  with pytest.raises(TypeError) as e:
    find_longest_word(42)
  assert str(e.value) == "'int' object is not iterable"
