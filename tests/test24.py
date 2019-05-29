import unittest, sys

sys.path = ['..', 'srcs']

from ex24 import make_3sg_form

class Test3sgForm(unittest.TestCase):

	def test_01(self):
		result = make_3sg_form('run')
		self.assertEqual(result, 'runs')

	def test_02(self):
		result = make_3sg_form('try')
		self.assertEqual(result, 'tries')

	def test_03(self):
		result = make_3sg_form('brush')
		self.assertEqual(result, 'brushes')

	def test_04(self):
		result = make_3sg_form('fix')
		self.assertEqual(result, 'fixes')

	def test_05(self):
		result = make_3sg_form('do')
		self.assertEqual(result, 'does')

	def test_06(self):
		result = make_3sg_form('batch')
		self.assertEqual(result, 'batches')

	def test_bad_type(self):
		data = 42
		with self.assertRaises(TypeError):
			result = make_3sg_form(data)
