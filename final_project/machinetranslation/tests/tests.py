import unittest
import sys
sys.path.append("..")
from ..translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(""), "")
        self.assertNotEqual(englishToFrench(""), " ")
    def test2(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertEqual(englishToFrench("Bonjour"),"Bonjour")
        self.assertNotEqual(englishToFrench( "Hello"), "Hello")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(""), "")
        self.assertNotEqual(frenchToEnglish(""), " ")
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(frenchToEnglish("Hello"), "Hello")
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")

unittest.main()