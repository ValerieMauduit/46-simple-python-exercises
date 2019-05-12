import unittest, sys

sys.path = ['..', 'srcs']

from ex11 import generate_n_chars

class TestGenChars(unittest.TestCase):
    def test_01(self):
        result = generate_n_chars(5, 'x')
        self.assertEqual(result, 'xxxxx')

    def test_02(self):
        result = generate_n_chars(10, 'a')
        self.assertEqual(result, 'aaaaaaaaaa')

    def test_bad_type(self):
        data = 'banana'
        with self.assertRaises(TypeError):
            result = sum(data)
