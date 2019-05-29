import unittest, sys

sys.path = ['..', 'srcs']

from ex15 import find_longest_word

class TestLongestWord(unittest.TestCase):

	def test_01(self):
		result = find_longest_word(['I', 'want', 'to', 'travel', 'to', 'Cambodia'])
		self.assertEqual(result, 8)

	def test_02(self):
		result = find_longest_word(['Python', 'is', 'cool'])
		self.assertEqual(result, 6)

	def test_bad_type(self):
		data = 42
		with self.assertRaises(TypeError):
			result = find_longest_word(data)
