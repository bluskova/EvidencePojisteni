"""
Konzolová aplikace pro evidenci pojistných událostí (pojištěných osob).

Aplikace obsahuje správu pojištěných (pojištěné osoby, např. "Jan Novák"):
Vytvoření pojištěného - eviduje se jméno, příjmení, věk a telefonní číslo
Zobrazení seznamu všech pojištěných
Vyhledání pojištěného - podle jména a příjmení

Dané entity jsou uloženy v paměti v kolekci "registry".
Ukládání dat po skončení aplikace se neřeší.
"""

from person import Person
from memory_storage import MemoryStorage
from db_storage import DbStorage
from utility_functions import *
from src.test_data import test_data


# registry = MemoryStorage()
registry = DbStorage()

# pridani pojistenych - testovaci data
for i in test_data:
    registry.add_person(i)


print('--------------------------------------')
print('Evidence pojištěných')
print('--------------------------------------')

end = False
while not end:
    print('\nVyberte akci:')
    print('1 - Přidat nového pojištěného')
    print('2 - Vypsat všechny pojištěné')
    print('3 - Vyhledat pojištěného')
    print('4 - Konec')
    instruction = input().strip()
    try:
        instruction = int(instruction)
        if instruction == 1:
            name, surname, age, phone = load_data(age=True, phone=True)
            if registry.is_person_registered(name, surname, age):
                print(f'\n{name} {surname} je již uložen v evidenci. ', end='')
            else:
                person = Person(name, surname, age, phone)
                registry.add_person(person)
                print(f'\nData byla uložena. ', end='')
            input(go_on)
        elif instruction == 2:
            if registry.number_of_records() > 0:
                print_persons_table(registry.get_all_persons())
            else:
                print('Evidence neobsahuje žádného pojištěného. ', end='')
            input(go_on)
        elif instruction == 3:
            name, surname = load_data()
            if not registry.is_person_registered(name, surname):
                print(f'\n{name} {surname} není v evidenci. ', end='')
            else:
                print_persons_table(registry.get_persons(name, surname))
            input(go_on)
        elif instruction == 4:
            end = True
        else:
            print(f'Zadal(a) jste {instruction}, prosím zadejte číslo 1 - 4!')
    except ValueError:
        print(f'Zadal(a) jste "{instruction}", prosím zadejte číslo!')
