import unittest, sys

sys.path = ['..', 'srcs']

from ex06 import mysum, multiply

class TestSumMultiply(unittest.TestCase):
    def test_sum(self):
        result = mysum([1, 2, 3, 4])
        self.assertEqual(result, 10)

    def test_multiply(self):
        result = (multiply([1, 2, 3, 4]))
        self.assertEqual(result, 24)

    def test_bad_type(self):
        data = 'banana'
        with self.assertRaises(TypeError):
            result = sum(data)
