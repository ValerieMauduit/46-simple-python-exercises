import pytest, sys

sys.path = ['..', 'srcs']

from ex24 import make_3sg_form

def test_make_3sg_form_01():
  result = make_3sg_form('run')
  assert result == 'runs'

def test_make_3sg_form_02():
  result = make_3sg_form('try')
  assert result == 'tries'

def test_make_3sg_form_03():
  result = make_3sg_form('brush')
  assert result == 'brushes'

def test_make_3sg_form_04():
  result = make_3sg_form('fix')
  assert result == 'fixes'

def test_make_3sg_form_05():
  result = make_3sg_form('do')
  assert result == 'does'

def test_make_3sg_form_06():
  result = make_3sg_form('batch')
  assert result == 'batches'

def test_make_3sg_form_bad_type():
  with pytest.raises(TypeError) as e:
    make_3sg_form(42)
  assert str(e.value) == "This function requires a string."
