import unittest
from translator import french_to_english, english_to_french

class TestFrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(null), null)
        self.assertEqual(french_to_english('Hello'), 'Bonjour')  



class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(null), null)
        self.assertEqual(englishToFrench('Bonjour'), 'Hello')  