import pytest, sys

sys.path = ['..', 'srcs']

from ex14 import words_to_len

def test_words_to_len_01():
  result = words_to_len(['I', 'want', 'to', 'sleep'])
  assert result == [1, 4, 2, 5]

def test_words_to_len_02():
  result = words_to_len(['Python', 'is', 'wonderful'])
  assert result == [6, 2, 9]

def test_words_to_len_bad_type():
  with pytest.raises(TypeError) as e:
    words_to_len(42)
  assert str(e.value) == "'int' object is not iterable"
