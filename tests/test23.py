import unittest, sys

sys.path = ['..', 'srcs']

from ex23 import correct

class TestCorrect(unittest.TestCase):
    def test_01(self):
        result = correct('This   is  very funny  and    cool.Indeed!')
        self.assertEqual(result, 'This is very funny and cool. Indeed!')

    def test_bad_type(self):
        data = 42
        with self.assertRaises(TypeError):
            result = sum(data)
