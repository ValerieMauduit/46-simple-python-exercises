import unittest, sys

sys.path = ['..', 'srcs']

from ex20 import translate

class TestTranslate(unittest.TestCase):
    
    def test_01(self):
        result = translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year'])
        self.assertEqual(result, ['god', 'jul', 'och', 'gott', 'nytt', 'år'])

    def test_bad_type(self):
        data = 42
        with self.assertRaises(TypeError):
            result = translate(data)
