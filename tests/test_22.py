import pytest, sys

sys.path = ['..', 'srcs']

from ex22 import rot13, create_key, merge_dicts

def test_rot13_01():
 result = rot13('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')
 assert result == 'Caesar cipher? I much prefer Caesar salad!'

def test_rot13_bad_type():
  with pytest.raises(TypeError) as e:
    rot13(42)
  assert str(e.value) == "'int' object is not iterable"
