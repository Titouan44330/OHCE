from datetime import datetime
from src.ohce import Ohce
now = datetime.now()
langue = "Anglais"
if __name__ == '__main__':
    print("Bonjour !")

    while (1):
        text = input('Saisissez un texte : ')
        if (text == 'quitter'):
            print("Au revoir !")
            break
        print(Ohce.miroir(text, langue))