class Zdalnie:

    def zwroc(cls, zdalne, repozytorium):
        repozytorium = input("Podaj link do repozytorium: ")
        return "git remote add origin "+ repozytorium
