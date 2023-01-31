import unittest
from src.ohce import Ohce

class OhceTest(unittest.TestCase) :
    def test_miroir(self) :
        # Quand on saisie une chaîne de caractère
        ohce = Ohce()
        res = ohce.miroir("toto")

        #Alors cette chaîne est renvoyé en miroir
        self.assertIn(res,"otot")

    def test_palindrome(self,mot):
        # Quand on saisit un palindrome
        ohce = Ohce()
        retour_palindrome = ohce.miroir(mot)

        # ALORS celui-ci est renvoyé
        self.assertIn(mot, retour_palindrome)

        # ET "Bien dit" est renvoyé ensuite
        self.assertIn("Bien dit",retour_palindrome)

    def test_bonjour_revoir(self, mot):
        # QUAND on saisit une chaine
        ohce = Ohce()
        retour = ohce.miroir(mot)

        # ALORS "Bonjour" est envoyé avant le mot et "Au revoir" est envoyé après.
        self.assertIn("Bonjour ", retour)
        self.assertIn(" Au revoir", retour)