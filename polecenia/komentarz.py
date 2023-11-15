class Komentarz:

    def zwroc(cls):
        komentarz = input("Podaj opis: ")
        return "git commit -m " + komentarz
