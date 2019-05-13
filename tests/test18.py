import unittest, sys

sys.path = ['..', 'srcs']

from ex18 import is_pangram

class TestIsPangram(unittest.TestCase):

    def test_01(self):
        result = is_pangram("The quick brown fox jumps over the lazy dog")
        self.assertEqual(result, True)

    def test_02(self):
        result = is_pangram("You are searching for a random sentence")
        self.assertEqual(result, False)

    def test_bad_type(self):
        data = 42
        with self.assertRaises(TypeError):
            result = is_pangram(data)
