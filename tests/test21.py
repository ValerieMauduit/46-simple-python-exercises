import unittest, sys

sys.path = ['..', 'srcs']

from ex21 import char_freq

class TestCharFreq(unittest.TestCase):

    def test_01(self):
        result = char_freq('abbabcbdbabdbdbabababcbcbab')
        self.assertEqual(result, {'a': 7, 'b': 14, 'c': 3, 'd': 3})

    def test_02(self):
        result = char_freq('abracadabra')
        self.assertEqual(result, {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

    def test_bad_type(self):
        data = 42
        with self.assertRaises(TypeError):
            result = char_freq(data)
