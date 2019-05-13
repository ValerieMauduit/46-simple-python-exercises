import unittest, sys

sys.path = ['..', 'srcs']

from ex13 import max_in_list

class TestMaxInList(unittest.TestCase):

    def test_01(self):
        result = max_in_list([4, 9, 7, 12, 42, 5])
        self.assertEqual(result, 42)

    def test_02(self):
        result = max_in_list([10.8, 4.2, 7.8, 12.4, 6.8])
        self.assertEqual(result, 12.4)

    def test_bad_type(self):
        data = 'banana'
        with self.assertRaises(TypeError):
            result = max_in_list(data)
