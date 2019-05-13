import unittest, sys

sys.path = ['..', 'srcs']

from ex17 import is_phrase_palindrome

class TestIsPhrasePalindrome(unittest.TestCase):

    def test_01(self):
        result = is_phrase_palindrome("Go hang a salami I'm a lasagna hog.")
        self.assertEqual(result, True)

    def test_02(self):
        result = is_phrase_palindrome("Dammit, I'm mad!")
        self.assertEqual(result, True)

    def test_03(self):
        result = is_phrase_palindrome("Where are the students?")
        self.assertEqual(result, False)

    def test_bad_type(self):
        data = 42
        with self.assertRaises(TypeError):
            result = is_phrase_palindrome(data)
