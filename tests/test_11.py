import pytest, sys

sys.path = ['..', 'srcs']

from ex11 import generate_n_chars

def test_generate_n_chars_01():
  result = generate_n_chars(5, 'x')
  assert result == 'xxxxx'

def test_generate_n_chars_02():
  result = generate_n_chars(10, 'a')
  assert result == 'aaaaaaaaaa'

def test_generate_n_chars_bad_type():
  with pytest.raises(TypeError) as e:
    generate_n_chars('banana', 'orange')
  assert str(e.value) == "can't multiply sequence by non-int of type 'str'"
