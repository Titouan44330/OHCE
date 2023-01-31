class Anglais() :
    def bonjour(heure):
        if (0 <= heure <= 4):
            return "Hello"
        elif 17 <= heure <= 23:
            return "Hello"
        elif 5 <= heure <= 16:
            return "Good morning"
        else :
            return "null"

    def au_revoir(heure):
        if 0 <= heure <= 4:
            return "Good night"
        elif 17 <= heure <= 23:
            return "Good night"
        elif 5 <= heure <= 16:
            return "Good bye"
        else :
            return "null"