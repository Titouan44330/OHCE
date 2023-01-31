import datetime
from src.langues.francais import Francais
from src.langues.anglais import Anglais


class Ohce:
    def miroir(self,mot, langue, heure):
        if langue == "Français" :
            miroir = mot[::-1]
            if mot == miroir:
                return miroir + " \n Bien dit !"
            return str(Francais.bonjour(heure))+" \n " + miroir + " \n "+str(Francais.au_revoir(heure))
        if langue == "Anglais":
            miroir = mot[::-1]
            if mot == miroir:
                return miroir + " \n Well done !"
            return str(Anglais.bonjour(heure))+" \n " + miroir + " \n "+str(Anglais.au_revoir(heure))
