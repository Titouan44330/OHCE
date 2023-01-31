from datetime import datetime
from src.ohce import Ohce
import locale
now = datetime.now()
langue = "Anglais"
heure = 13
if __name__ == '__main__':
    print("Bonjour !")

    while (1):
        text = input('Saisissez un texte : ')
        if (text == 'quitter' or text == 'quit'):
            print("Au revoir !")
            break
        print(Ohce.miroir(locale, text, langue, heure))