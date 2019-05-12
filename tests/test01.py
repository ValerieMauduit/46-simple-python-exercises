import unittest, sys

sys.path = ['..', 'srcs']

from ex01 import mymax

class TestMax(unittest.TestCase):
    def test_01(self):
        result = max(2, 8)
        self.assertEqual(result, 8)

    def test_02(self):
        result = max(6.8, 0.3)
        self.assertEqual(result, 6.8)

    def test_bad_type(self):
        data = 'banana'
        with self.assertRaises(TypeError):
            result = sum(data)
