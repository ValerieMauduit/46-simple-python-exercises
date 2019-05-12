import unittest, sys

sys.path = ['..', 'srcs']

from ex10 import overlapping

class TestOverlapping(unittest.TestCase):
    def test_01(self):
        result = overlapping([0, 1, 2, 3, 4, 5], ['hello world', 42])
        self.assertEqual(result, False)

    def test_02(self):
        result = overlapping([0, 1, 2, 3, 4, 5], [4, 2, 42, 4.2])
        self.assertEqual(result, True)

    def test_03(self):
        result = overlapping(['hello world', 42], [4, 2, 42, 4.2])
        self.assertEqual(result, True)

    def test_bad_type(self):
        data = 'banana'
        with self.assertRaises(TypeError):
            result = sum(data)
