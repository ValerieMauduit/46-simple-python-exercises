import unittest, sys

sys.path = ['..', 'srcs']

from ex08 import is_palindrome

class TestIsPalindrome(unittest.TestCase):

	def test_01(self):
		result = is_palindrome('radar')
		self.assertEqual(result, True)

	def test_02(self):
		result = is_palindrome('hello')
		self.assertEqual(result, False)

	def test_bad_type(self):
		data = 42
		with self.assertRaises(TypeError):
			result = is_palindrome(data)
