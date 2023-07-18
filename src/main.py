"""Konzolová aplikace pro evidenci pojistných událostí.

Aplikace obsahuje správu pojištěných (to jsou pojištěné osoby, např. "Jan Novák"):
Vytvoření pojištěného
Evidujte jméno, příjmení, věk a telefonní číslo
Zobrazení seznamu všech pojištěných
Vyhledání pojištěného podle jména a příjmení
Dané entity jsou uloženy v kolekci v paměti
Aplikace je naprogramována podle dobrých praktik
Využívejte konstruktory pro inicializaci objektů
toString() pro jejich výpis
Oddělujte kód do samostatných tříd a souborů
Editaci a odstranění pojištěných ani ukládání dat po skončení aplikace není třeba řešit."""


from pojisteny import Pojisteny
from funkce import *


evidence = []

# # pridani pojistenych - testovaci data
# pojisteny = Pojisteny('Jan', 'Novak', 35, 775141988)
# evidence.append(pojisteny)
# pojisteny = Pojisteny('Ales', 'Luska', 4, 728582450)
# evidence.append(pojisteny)
# pojisteny = Pojisteny('Ales', 'Luska', 88, 728582450)
# evidence.append(pojisteny)

print('--------------------------------------')
print('Evidence pojištěných')
print('--------------------------------------')

konec = False
while not konec:
    print('\nVyberte akci:')
    print('1 - Přidat nového pojištěného')
    print('2 - Vypsat všechny pojištěné')
    print('3 - Vyhledat pojištěného')
    print('4 - Konec')
    prikaz = input().strip()
    print()
    try:
        prikaz = int(prikaz)
        if prikaz == 1:
            jmeno, prijmeni, vek, telefon = nacti_udaje(vek_nacist=True, telefon_nacist=True)
            if je_v_evidenci(evidence, jmeno, prijmeni, vek):
                print(f'\n{jmeno} {prijmeni}, věk {vek} je již uložen v evidenci. ', end='')
                input(pokracujte)
            else:
                pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
                evidence.append(pojisteny)
                print(f'\nData byla uložena. ', end='')
                input(pokracujte)
        elif prikaz == 2:
            if len(evidence) > 0:
                vypis_evidenci(evidence)
            else:
                print('Evidence neobsahuje žádného pojištěného. ',)
            input(pokracujte)
        elif prikaz == 3:
            jmeno, prijmeni = nacti_udaje()
            if not je_v_evidenci(evidence, jmeno, prijmeni):
                print(f'\n{jmeno} {prijmeni} není v evidenci.')
            else:
                vypis_evidenci(evidence, jmeno, prijmeni)
            input(pokracujte)
        elif prikaz == 4:
            konec = True
        else:
            print(f'Zadal(a) jste {prikaz}, prosím zadete číslo 1 - 4!')
    except ValueError:
        print(f'Zadal(a) jste "{prikaz}", prosím zadete číslo!')
