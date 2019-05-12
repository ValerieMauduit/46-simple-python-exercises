import unittest, sys

sys.path = ['..', 'srcs']

from ex03 import length

class TestLength(unittest.TestCase):
    def test_01(self):
        result = length('Hello world!')
        self.assertEqual(result, 12)

    def test_02(self):
        result = length([0, 1, 2, 3, 4, 5])
        self.assertEqual(result, 6)

    def test_bad_type(self):
        data = 42
        with self.assertRaises(TypeError):
            result = sum(data)
