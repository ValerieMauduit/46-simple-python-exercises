import unittest, sys

sys.path = ['..', 'srcs']

from ex12 import histogram

class TestHistogram(unittest.TestCase):

	def test_01(self):
		result = histogram([4, 9, 7])
		hist = '''****\n*********\n*******'''
		self.assertEqual(result, hist)

	def test_02(self):
		result = histogram([1, 2, 3, 4])
		hist = '''*\n**\n***\n****'''
		self.assertEqual(result, hist)

	def test_bad_type(self):
		data = 'banana'
		with self.assertRaises(TypeError):
			result = histogram(data)
