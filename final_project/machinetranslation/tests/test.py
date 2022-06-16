import unittest
from translator import englishtofrench, frenchtoenglish

class TestsEnglishToFrench(unittest.TestCase):
    def test1(self): 
        self.assertIsNone(englishtofrench(None))
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertNotEqual(englishtofrench("Bonjour"), "Hello")
class TestsFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNone(frenchtoenglish(None))
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchtoenglish("Hello"), "Bonjour")

unittest.main()