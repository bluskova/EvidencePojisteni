from typing import List

from src.person import Person

name_max_len = 15
go_on = 'Pokračujte stisknutím klávesy Enter...'


def load_name(surname=None):
    name_ok = False
    while not name_ok:
        name = input(f'Zadejte {"příjmení" if surname else "jméno pojištěného"}: ').strip()
        if name.isalpha() and 1 < len(name) < name_max_len:
            name = name.title()
            name_ok = True
        else:
            print(f'Nesprávný formát. Použijte minimálně 2, maximálně {name_max_len} znaků [a - ž].')
    return name


def load_age():
    age_ok = False
    while not age_ok:
        age = input('Zadejte věk: ')
        try:
            age = int(age)
            if 0 <= age <= 130:
                age_ok = True
            else:
                print(f'Zadal(a) jste {age}. Prosím zadejte věk v rozmezí 0 - 130.')
        except ValueError:
            print(f'Zadal(a) jste "{age}". Prosím zadejte číslo [0 - 130].')
    return age


def load_phone():
    phone_ok = False
    while not phone_ok:
        phone = input('Zadejte telefonní číslo: ')
        try:
            phone = int(phone.replace(' ', ''))
            if len(str(phone)) == 9:
                phone_ok = True
            else:
                print(f'Nesprávná délka telefonního čísla. Prosím zadejte 9-místné telefonní číslo (bez předvolby).')
        except ValueError:
            print(f'Zadal(a) jste "{phone}". Prosím zadejte pouze číslice [0 - 9].')
    return phone


def load_data(age=False, phone=False):
    print()
    data = [load_name(), load_name(surname=True)]
    if age:
        data.append(load_age())
    if phone:
        data.append(load_phone())
    return data


def get_person_text_row(person: Person):
    return f'{person.get_name(): <{name_max_len}}{person.get_surname(): <{name_max_len}}' \
           f'{person.get_age(): <{name_max_len}}{person.get_phone(): <{name_max_len}}'


def print_persons_table(persons_list: List[Person]):
    head = "".join(column.ljust(name_max_len) for column in ['Jméno', 'Příjmení', 'Věk', 'Telefonní číslo'])
    print(head)
    for person in persons_list:
        print(get_person_text_row(person))
