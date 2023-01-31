class Francais :
    def bonjour(heure) :
        if 0 <= heure <= 4:
            return "Bonsoir"
        elif 17 <= heure <= 23:
            return "Bonsoir"
        elif 5<= heure <= 16:
            return "Bonjour"
        else :
            return "null"

    def au_revoir(heure) :
        if 0 <= heure <= 4 and 17 <= heure <= 23:
            return "Bonne soirée"
        elif 17 <= heure <= 23 :
            return "Bonne soirée"
        elif 5<= heure <= 16:
            return "Bonne journée"
        else :
            return "null"