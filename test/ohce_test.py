import unittest
from src.ohce import Ohce

class OhceTest(unittest.TestCase) :
    def test_miroir(self) :
        # Quand on saisie une chaîne de caractère
        ohce = Ohce()
        res = ohce.miroir("toto")

        #Alors cette chaîne est renvoyé en miroir
        self.assertEqual(res,"otot")

    def test_palindrome(self):
        ohce = Ohce()
        res = ohce.miroir("radar")
        self.assertEqual("radar",res)