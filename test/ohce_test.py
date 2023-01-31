import unittest
from src.ohce import Ohce

class OhceTest(unittest.TestCase) :
    def test_miroir(self) :
        # Quand on saisie une chaîne de caractère
        ohce = Ohce()
        res = ohce.miroir("toto","Français")

        #Alors cette chaîne est renvoyé en miroir
        self.assertIn(res,"otot")

    def test_palindrome_francais(self):
        # Quand on saisit un palindrome
        ohce = Ohce()
        mot = "radar"
        retour_palindrome = ohce.miroir("radar","Français")

        # ALORS celui-ci est renvoyé
        self.assertIn(mot, retour_palindrome)

        # ET "Bien dit" est renvoyé ensuite en Français
        self.assertIn("Bien dit",retour_palindrome)

    def test_palindrome_anglais(self):
        # Quand on saisit un palindrome
        ohce = Ohce()
        mot = "radar"
        retour_palindrome = ohce.miroir("radar", "Anglais")

        # ALORS celui-ci est renvoyé
        self.assertIn(mot, retour_palindrome)

        # ET "Well done" est renvoyé ensuite en Anglais
        self.assertIn("Well done", retour_palindrome)

    def test_bonjour_revoir_francais(self):
        # QUAND on saisit une chaine
        ohce = Ohce()
        mot = "Et oui jamie"
        retour = ohce.miroir(mot,"Français")

        # ALORS "Bonjour" est envoyé avant le mot et "Au revoir" est envoyé après.
        self.assertIn("Bonjour ", retour)
        self.assertIn(" Au revoir", retour)

    def test_bonjour_revoir_anglais(self):
        # QUAND on saisit une chaine
        ohce = Ohce()
        mot = "Et oui jamie"
        retour = ohce.miroir(mot,"Anglais")

        # ALORS "Hello" est envoyé avant le mot et "Good bye" est envoyé après.
        self.assertIn("Hello ", retour)
        self.assertIn(" Good bye", retour)
