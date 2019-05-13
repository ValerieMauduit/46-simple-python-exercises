import unittest, sys

sys.path = ['..', 'srcs']

from ex22 import rot13, create_key, merge_dicts

class TestCaesar(unittest.TestCase):
    
    def test_01(self):
        result = rot13('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')
        self.assertEqual(result, 'Caesar cipher? I much prefer Caesar salad!')

    def test_bad_type(self):
        data = 42
        with self.assertRaises(TypeError):
            result = rot13(data)
