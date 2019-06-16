import pytest, sys

sys.path = ['..', 'srcs']

from ex16 import filter_long_words

def test_filter_long_words_01():
  result = filter_long_words(['I', 'want', 'to', 'travel', 'to', 'Cambodia'], 2)
  assert result == ['want', 'travel', 'Cambodia']

def test_filter_long_words_02():
  result = filter_long_words(['Python', 'is', 'cool'], 3)
  assert result == ['Python', 'cool']

def test_filter_long_words_bad_type():
  with pytest.raises(TypeError) as e:
    filter_long_words(42, 3)
  assert str(e.value) == "'int' object is not iterable"
