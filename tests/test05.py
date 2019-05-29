import unittest, sys

sys.path = ['..', 'srcs']

from ex05 import translate

class TestTranslate(unittest.TestCase):

	def test_01(self):
		result = translate('this is fun')
		self.assertEqual(result, 'tothohisos isos fofunon')

	def test_02(self):
		result = translate('Hello World')
		self.assertEqual(result, 'HoHelollolo WoWororloldod')

	def test_bad_type(self):
		data = 42
		with self.assertRaises(TypeError):
			result = translate(data)
