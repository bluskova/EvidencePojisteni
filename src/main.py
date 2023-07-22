"""
Konzolová aplikace pro evidenci pojištěných osob.

Aplikace obsahuje správu pojištěných (pojištěné osoby, např. "Jan Novák"):
Každou osobu jednoznačně identifikuje jméno, příjmení a věk.
Evidence nabízí:
    Zobrazení seznamu všech pojištěných
    Vyhledání pojištěného - podle jména a příjmení, v případě shody podle věku
    Přidání pojištěného - eviduje se jméno, příjmení, věk a telefonní číslo
    Odstranění pojištěného - podle jména a příjmení, v případě shody podle věku

Podle volby uživatele jsou dané entity uloženy buď v databázi anebo v paměti v kolekci.
Aplikace uživateli nabízí vložení testovacích dat do evidence.

Ukládání dat po skončení aplikace se neřeší.
Po skončení aplikace zůstanou data buď uložena v databázovém souboru při použití databáze.
"""

from data_storage.db_storage import DbStorage
from data_storage.memory_storage import MemoryStorage
from utility_functions import *
from src.test_data import test_data
from sqlite3 import Error as SQLError


print(*REGISTRY_MAIN, sep='\n')

print()
use_database = input('Chcete použít databázi? [ano / ne]: ').strip()
if use_database == 'ano':
    registry = DbStorage()
    print(f'Evidence pojištěných je vytvořena. Data jsou uložena v souboru "{DbStorage.db_file}". ', end='')
else:
    registry = MemoryStorage()
    print('Evidence pojištěných je vytvořena. Data budou uložena v paměti, po ukončení programu smazána. ', end='')
input(GO_ON_TEXT)

print()
use_test_data = input('Chcete do evidence vložit testovací data? [ano / ne]: ').strip()
try:
    if use_test_data == 'ano':
        for person in test_data:
            if not registry.is_person_registered(person.get_name(), person.get_surname(), person.get_age()):
                registry.add_person(person)
        print('Testovací data jsou uložena v evidenci. ', end='')
    print('Evidence je připravena k použití. ', end='')
    input(GO_ON_TEXT)
except SQLError:
    print('Chyba databáze při vkládání testovacích dat.')

end = False
while not end:
    print()
    print(*INSTRUCTIONS_TEXT, sep='\n')
    instruction = input().strip()
    try:
        instruction = int(instruction)
        if instruction == 1:
            if registry.number_of_records() > 0:
                print_persons_table(registry.get_all_persons())
            else:
                print(EMPTY_REGISTRY_TEXT, end='')
            input(GO_ON_TEXT)
        elif instruction == 2:
            name, surname = load_person_data()
            if not registry.is_person_registered(name, surname):
                print()
                print(get_not_in_evidence_text(name, surname), end='')
            else:
                print_persons_table(registry.get_persons(name, surname))
            input(GO_ON_TEXT)
        elif instruction == 3:
            name, surname, age, phone = load_person_data(use_age=True, use_phone=True)
            if registry.is_person_registered(name, surname, age):
                print(get_is_in_evidence_text(name, surname, age), end='')
            else:
                person = Person(name, surname, age, phone)
                registry.add_person(person)
                print()
                print(DATA_SAVED_TEXT, end='')
            input(GO_ON_TEXT)
        elif instruction == 4:
            name, surname = load_person_data()
            if registry.count_person_registered(name, surname) == 0:
                print(get_not_in_evidence_text(name, surname), end='')
            elif registry.count_person_registered(name, surname) == 1:
                registry.remove_person(name, surname)
                print(get_removed_text(name, surname), end='')
            else:
                print()
                print(MORE_RECORDS_TEXT)
                print_persons_table(registry.get_persons(name, surname))
                age = load_age()
                if registry.is_person_registered(name, surname, age):
                    registry.remove_person(name, surname, age)
                    print(get_removed_text(name, surname, age), end='')
                else:
                    print(get_not_in_evidence_text(name, surname, age), end='')
            input(GO_ON_TEXT)
        elif instruction == 5:
            end = True
        else:
            print(get_bad_instructions_text(instruction))
    except ValueError:
        print(get_bad_instructions_text(instruction))
    except SQLError:
        print('Chyba databáze. ')
