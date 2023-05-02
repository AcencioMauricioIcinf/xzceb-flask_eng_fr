from unittest import TestCase, main
from translator import english_to_french, french_to_english

class TestEnFrTranslation(TestCase):
    def test1(self):
        self.assertRaises(ValueError, english_to_french, None)
    def test2(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrEnTranslation(TestCase):
    def test1(self):
        self.assertRaises(ValueError, french_to_english, None)
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

main()