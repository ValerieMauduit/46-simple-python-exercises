import unittest, sys

sys.path = ['..', 'srcs']

from ex16 import filter_long_words

class TestFilterWords(unittest.TestCase):
    
    def test_01(self):
        result = filter_long_words(['I', 'want', 'to', 'travel', 'to', 'Cambodia'], 2)
        self.assertEqual(result, ['want', 'travel', 'Cambodia'])

    def test_02(self):
        result = filter_long_words(['Python', 'is', 'cool'], 3)
        self.assertEqual(result, ['Python', 'cool'])

    def test_bad_type(self):
        data = 42
        with self.assertRaises(TypeError):
            result = filter_long_words(data)
