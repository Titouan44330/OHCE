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
else :
    langue = "NONE"

if __name__ == '__main__':
    print("Bonjour !")

    while (1):
        text = input('Saisissez un texte : ')
        if (text == 'quitter' or text == 'quit' or langue == "NONE"):
            if langue == "NONE":
                print("La langue de votre système n'est pas géré par le logiciel !")
            print("Au revoir !")
            break
        print(Ohce.miroir(locale, text, langue, now.hour))