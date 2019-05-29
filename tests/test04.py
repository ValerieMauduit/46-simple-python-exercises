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

	def test_bad_type(self):
		data = 42
		with self.assertRaises(TypeError):
			result = is_vowel(data)

	def test_bad_len(self):
		data = 'banana'
		with self.assertRaises(ValueError):
			result = is_vowel(data)
