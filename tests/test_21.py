import pytest, sys

sys.path = ['..', 'srcs']

from ex21 import char_freq

def test_char_freq_01():
  result = char_freq('abbabcbdbabdbdbabababcbcbab')
  assert result == {'a': 7, 'b': 14, 'c': 3, 'd': 3}

def test_char_freq_02():
  result = char_freq('abracadabra')
  assert result == {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

def test_char_freq_bad_type():
  with pytest.raises(TypeError) as e:
    char_freq(42)
  assert str(e.value) == "'int' object is not iterable"
