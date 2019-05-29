import unittest, sys

sys.path = ['..', 'srcs']

from ex10 import overlapping

lst1 = [0, 1, 2, 3, 4, 5]
lst2 = ['hello world', 42]
lst3 = [4, 2, 42, 4.2]

class TestOverlapping(unittest.TestCase):

	def test_01(self):
		result = overlapping(lst1, lst2)
		self.assertEqual(result, False)

	def test_02(self):
		result = overlapping(lst1, lst3)
		self.assertEqual(result, True)

	def test_03(self):
		result = overlapping(lst2, lst3)
		self.assertEqual(result, True)

	def test_bad_type(self):
		data = 'banana'
		with self.assertRaises(TypeError):
			result = overlapping(data)
