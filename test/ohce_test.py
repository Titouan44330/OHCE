import unittest
from src.ohce import Ohce

class OhceTest(unittest.TestCase) :
    def test_miroir(self) :
        # Quand on saisie une chaîne de caractère
        ohce = Ohce()
        res = ohce.miroir("toto","Français",13)

        #Alors cette chaîne est renvoyé en miroir
        self.assertIn("otot",res)

    def test_palindrome_francais(self):
        # Quand on saisit un palindrome
        ohce = Ohce()
        mot = "radar"
        retour_palindrome = ohce.miroir("radar","Français",13)

        # ALORS celui-ci est renvoyé
        self.assertIn(mot, retour_palindrome)

        # ET "Bien dit" est renvoyé ensuite en Français
        self.assertIn("Bien dit",retour_palindrome)

    def test_palindrome_anglais(self):
        # Quand on saisit un palindrome
        ohce = Ohce()
        mot = "radar"
        retour_palindrome = ohce.miroir("radar", "Anglais",13)

        # ALORS celui-ci est renvoyé
        self.assertIn(mot, retour_palindrome)

        # ET "Well done" est renvoyé ensuite en Anglais
        self.assertIn("Well done", retour_palindrome)

    def test_salutation_journée_francais(self):
        # QUAND on saisit une chaine
        ohce = Ohce()
        mot = "Et oui jamie"
        retour = ohce.miroir(mot,"Français",13)

        # ALORS "Bonjour" est envoyé avant le mot et "Au revoir" est envoyé après.
        self.assertIn("Bonjour", retour)
        self.assertIn("Bonne journée", retour)

    def test_salutation_soir_francais(self):
        # QUAND on saisit une chaine
        ohce = Ohce()
        mot = "Et oui jamie"
        retour = ohce.miroir(mot,"Français",20)

        # ALORS "Bonjour" est envoyé avant le mot et "Au revoir" est envoyé après.
        self.assertIn("Bonsoir", retour)
        self.assertIn("Bonne soirée", retour)

    def test_salutation_morning_anglais(self):
        # QUAND on saisit une chaine
        ohce = Ohce()
        mot = "And yes jamie"
        retour = ohce.miroir(mot,"Anglais",13)

        # ALORS "Hello" est envoyé avant le mot et "Good bye" est envoyé après.
        self.assertIn("Good morning", retour)
        self.assertIn("Good bye", retour)
    def test_salutation_night_anglais(self):
        # QUAND on saisit une chaine
        ohce = Ohce()
        mot = "And yes jamie"
        retour = ohce.miroir(mot,"Anglais",20)

        # ALORS "Hello" est envoyé avant le mot et "Good bye" est envoyé après.
        self.assertIn("Hello", retour)
        self.assertIn("Good night", retour)

if __name__ == '__main__':
    unittest.main()