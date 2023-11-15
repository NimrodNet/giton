class Dodaj_z_komentarzem:

    def zwroc(cls):
        komentarz = input("Dodaj opis: ")
        return "git commit -a -m " + komentarz
