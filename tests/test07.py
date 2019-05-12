import unittest, sys

sys.path = ['..', 'srcs']

from ex07 import reverse

class TestReverse(unittest.TestCase):
    def test_01(self):
        result = reverse('I am testing')
        self.assertEqual(result, 'gnitset ma I')

    def test_02(self):
        result = reverse('Hello World')
        self.assertEqual(result, 'dlroW olleH')

    def test_bad_type(self):
        data = 42
        with self.assertRaises(TypeError):
            result = sum(data)
