import pytest, sys

sys.path = ['..', 'srcs']

from ex20 import translate

def test_translate_01():
  result = translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year'])
  assert result == ['god', 'jul', 'och', 'gott', 'nytt', 'år']

def test_translate_bad_type():
  with pytest.raises(TypeError) as e:
    translate(42)
  assert str(e.value) == "'int' object is not iterable"
