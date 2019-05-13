import unittest, sys

sys.path = ['..', 'srcs']

from ex04 import is_vowel

class TestIsVowel(unittest.TestCase):

    def test_01(self):
        result = is_vowel('a')
        self.assertEqual(result, True)

    def test_02(self):
        result = is_vowel('b')
        self.assertEqual(result, False)
