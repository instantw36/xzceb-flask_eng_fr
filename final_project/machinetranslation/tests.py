"""Tests"""
import unittest
from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    """Test for english to french"""
    def test1(self):
        """test 1"""
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("Fish"),"Poissons")
        self.assertNotEqual(english_to_french("February"),"Janvier")

class TestfrenchToEnglish(unittest.TestCase):
    """Test for french to english"""
    def test1(self):
        """test 1"""
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("salle de bains"), "Bathroom")
        self.assertNotEqual(french_to_english("Sebone"), "Seaborne")
unittest.main()
