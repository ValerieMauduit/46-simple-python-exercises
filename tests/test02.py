import unittest, sys

sys.path = ['..', 'srcs']

from ex02 import max_of_three

class TestMaxOfThree(unittest.TestCase):
    def test_01(self):
        result = max_of_three(2, 6, 42)
        self.assertEqual(result, 42)

    def test_m02(self):
        result = max_of_three(10.8, 5.4, 0.1)
        self.assertEqual(result, 10.8)

    def test_bad_type(self):
        data = 'banana'
        with self.assertRaises(TypeError):
            result = max_of_three(data)
