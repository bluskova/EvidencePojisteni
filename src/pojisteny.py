from funkce import max_delka_jmena

class Pojisteny:

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return(f'{self.jmeno: <{max_delka_jmena}}{self.prijmeni: <{max_delka_jmena}}{self.vek: <{max_delka_jmena}}'
               f'{self.telefon: <{max_delka_jmena}}')
