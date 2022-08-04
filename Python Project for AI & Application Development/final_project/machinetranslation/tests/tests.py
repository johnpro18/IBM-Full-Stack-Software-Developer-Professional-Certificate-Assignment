import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """Class for English To French"""
    def test_english_to_french(self):
        """Function for English To French"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class TestFrenchTpEnglish(unittest.TestCase):
    """Class for French To English"""
    def test_french_to_english(self):
        """Function for French To English"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()