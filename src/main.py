"""
Konzolová aplikace pro evidenci pojistných událostí (pojištěných osob).

Aplikace obsahuje správu pojištěných (pojištěné osoby, např. "Jan Novák"):
Vytvoření pojištěného - eviduje se jméno, příjmení, věk a telefonní číslo
Zobrazení seznamu všech pojištěných
Vyhledání pojištěného - podle jména a příjmení

Dané entity jsou uloženy v paměti v kolekci "registry".
Ukládání dat po skončení aplikace se neřeší.
"""

from tests import DbStorage
from utility_functions import *
from src.test_data import test_data


# registry = MemoryStorage()
registry = DbStorage()

# pridani pojistenych - testovaci data
for person in test_data:
    if not registry.is_person_registered(person.get_name(), person.get_surname(), person.get_age()):
        registry.add_person(person)


print('--------------------------------------')
print('Evidence pojištěných')
print('--------------------------------------')

end = False
while not end:
    print()
    for i in INSTRUCTIONS_TEXT:
        print(i)
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
            name, surname = load_data()
            if not registry.is_person_registered(name, surname):
                print()
                print(get_not_in_evidence_text(name, surname), end='')
            else:
                print_persons_table(registry.get_persons(name, surname))
            input(GO_ON_TEXT)
        elif instruction == 3:
            name, surname, age, phone = load_data(use_age=True, use_phone=True)
            if registry.is_person_registered(name, surname, age):
                print(get_is_in_evidence_text(name, surname, age), end='')
            else:
                person = Person(name, surname, age, phone)
                registry.add_person(person)
                print()
                print(DATA_SAVED_TEXT, end='')
            input(GO_ON_TEXT)
        elif instruction == 4:
            name, surname = load_data()
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
            pass
        elif instruction == 6:
            end = True
        else:
            print(get_bad_instructions_text(instruction))
    except ValueError:
        print(get_bad_instructions_text(instruction))
