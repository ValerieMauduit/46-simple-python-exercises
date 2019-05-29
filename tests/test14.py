import unittest, sys

sys.path = ['..', 'srcs']

from ex14 import words_to_len

class TestWordToLen(unittest.TestCase):

	def test_01(self):
		result = words_to_len(['I', 'want', 'to', 'sleep'])
		self.assertEqual(result, [1, 4, 2, 5])

	def test_02(self):
		result = words_to_len(['Python', 'is', 'wonderful'])
		self.assertEqual(result, [6, 2, 9])

	def test_bad_type(self):
		data = 42
		with self.assertRaises(TypeError):
			result = words_to_len(data)
