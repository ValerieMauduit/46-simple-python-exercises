import pytest, sys

sys.path = ['..', 'srcs']

from ex05 import translate

def test_translate_01():
  result = translate('this is fun')
  assert result == 'tothohisos isos fofunon'

def test_translate_02():
  result = translate('Hello World')
  assert result == 'HoHelollolo WoWororloldod'

def test_translate_bad_type():
  with pytest.raises(TypeError) as e:
    translate(42)
  assert str(e.value) == "'int' object is not iterable"
