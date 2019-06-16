import pytest, sys

sys.path = ['..', 'srcs']

from ex07 import reverse

def test_reverse_01():
  result = reverse('I am testing')
  assert result == 'gnitset ma I'

def test_reverse_02():
  result = reverse('Hello World')
  assert result == 'dlroW olleH'

def test_reverse_bad_type():
  with pytest.raises(TypeError) as e:
    reverse(42)
  assert str(e.value) == "'int' object is not subscriptable"
