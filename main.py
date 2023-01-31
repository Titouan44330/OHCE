from datetime import datetime
from src.ohce import Ohce
import locale
now = datetime.now()
langue = ""
langue_systeme = locale.getdefaultlocale()[0]
if langue_systeme == "fr":
    langue = "Français"
elif langue_systeme == "en_GB":
    langue = "Anglais"

if __name__ == '__main__':
    print("Bonjour !")

    while (1):
        text = input('Saisissez un texte : ')
        if (text == 'quitter' or text == 'quit'):
            print("Au revoir !")
            break
        print(Ohce.miroir(locale, text, langue, now.hour))