import unittest, sys

sys.path = ['..', 'srcs']

from ex09 import is_member

class TestIsMember(unittest.TestCase):

	def test_01(self):
		result = is_member('a', [0, 1, 2, 3, 4, 5])
		self.assertEqual(result, False)

	def test_02(self):
		result = is_member(1, [0, 1, 2, 3, 4, 5])
		self.assertEqual(result, True)

	def test_03(self):
		result = is_member('hello', ['hello', 'world'])
		self.assertEqual(result, True)

	def test_bad_type(self):
		data = 'banana'
		with self.assertRaises(TypeError):
			result = is_member(data)
