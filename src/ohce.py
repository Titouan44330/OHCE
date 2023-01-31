class Ohce:
    def miroir(self, mot, langue):
        miroir = mot[::-1]
        if mot == miroir:
            if langue == "Français" :
                return miroir + " \n Bien dit"
            else :
                return miroir + " \n Well done !"
        if langue == "Français":
            return "Bonjour \n " + miroir + "\n Au revoir"
        else :
            return "Hello \n " + miroir + "\n Good Bye"
