"""
Konzolová aplikace pro evidenci pojištěných osob.

Aplikace obsahuje správu pojištěných (pojištěné osoby, např. "Jan Novák").
Každou osobu jednoznačně identifikuje jméno, příjmení a věk
(dvě osoby, které mají shodné jméno, příjmení i věk nemohou být zaevidovány).

Evidence nabízí:
Zobrazení seznamu všech pojištěných
Vyhledání pojištěného - podle jména a příjmení, v případě shody podle věku
Přidání pojištěného - eviduje se jméno, příjmení, věk a telefonní číslo
Odstranění pojištěného - podle jména a příjmení, v případě shody podle věku
Ukončení evidence

Podle volby uživatele jsou dané entity uloženy buď v databázi anebo v paměti v kolekci.
Aplikace uživateli nabízí vložení testovacích dat do evidence.
Defaultní nastavení je ukládání kolekce do paměti bez použití testovacích osob.

V případě použití databáze jsou data po skončení aplikace uložena v souboru "registry.db".
V případě ukládání entit do paměti aplikace uložení dat po skončení aplikace neřeší.
"""

from data_storage.db_storage import DbStorage
from data_storage.memory_storage import MemoryStorage
from utility_functions import *
from src.test_data import test_data
from sqlite3 import Error as SQLError


print(*REGISTRY_MAIN, sep='\n')

use_database = get_instructions_bool('Chcete použít databázi?')
if use_database:
    registry = DbStorage()
else:
    registry = MemoryStorage()
print(get_evidence_created_text(use_database))
input(GO_ON_TEXT)

use_test_data = get_instructions_bool('Chcete do evidence vložit testovací data?')
if use_test_data:
    try:
        for person in test_data:
            if not registry.is_person_registered(person.get_name(), person.get_surname(), person.get_age()):
                registry.add_person(person)
    except SQLError:
        print(DATABASE_ERROR_TEXT)
print(get_insert_test_data_text(use_test_data))
input(GO_ON_TEXT)

end = False
while not end:
    print()
    print(*INSTRUCTIONS_TEXT, sep='\n')
    instruction = input().strip()
    try:
        instruction = int(instruction)
        print()
        if instruction == 1:
            if registry.number_of_records() > 0:
                print_persons_table(registry.get_all_persons())
            else:
                print(EMPTY_REGISTRY_TEXT, end='')
            input(GO_ON_TEXT)
        elif instruction == 2:
            name, surname = load_person_data()
            if not registry.is_person_registered(name, surname):
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
            if not registry.is_person_registered(name, surname):
                print(get_not_in_evidence_text(name, surname), end='')
            elif registry.count_person_registered(name, surname) == 1:
                registry.remove_person(name, surname)
                print(get_removed_text(name, surname), end='')
            else:
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
            print(get_end_of_database_text(use_database))
        else:
            print(get_bad_instructions_text(instruction))
    except ValueError:
        print(get_bad_instructions_text(instruction))
    except SQLError:
        print(DATABASE_ERROR_TEXT)
