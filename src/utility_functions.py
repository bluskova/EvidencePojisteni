from typing import List, Optional

from src.person import Person

REGISTRY_MAIN = [ '--------------------------------------', 'Evidence pojištěných',
                 '--------------------------------------']
GO_ON_TEXT = 'Pokračujte stisknutím klávesy Enter... '
DATA_SAVED_TEXT = 'Data byla uložena. '
EMPTY_REGISTRY_TEXT = 'Evidence neobsahuje žádného pojištěného. '
MORE_RECORDS_TEXT = 'V evidenci je více záznamů se zadaným jménem a příjmením. Zadejte věk osoby, kterou chcete ' \
                    'odstranit. '
INSTRUCTIONS_TEXT = ['Vyberte akci:', '1 - Vypsat všechny pojištěné', '2 - Vyhledat pojištěného',
                     '3 - Přidat pojištěného', '4 - Odstranit pojištěného', '5 - Konec']


def get_common_log_text(name: str, surname: str, age: Optional[int] = None):
    text = name + ' ' + surname
    if age:
        text += ', věk ' + str(age)
    return text


def get_is_in_evidence_text(name: str, surname: str, age: Optional[int] = None):
    return get_common_log_text(name, surname, age) + ' je již uložen v evidenci. '


def get_not_in_evidence_text(name: str, surname: str, age: Optional[int] = None):
    return get_common_log_text(name, surname, age) + ' není v evidenci. '


def get_removed_text(name: str, surname: str, age: Optional[int] = None):
    return get_common_log_text(name, surname, age) + ' byl odstraněn. '


def get_bad_instructions_text(instruction: str):
    return f'Zadal(a) jste {instruction}, prosím zadejte číslo 1 - 6!'


def load_name(use_surname: Optional[bool] = None):
    name_ok = False
    name = None
    while not name_ok:
        name = input(f'Zadejte {"příjmení" if use_surname else "jméno pojištěného"}: ').strip()
        if name.isalpha() and 1 < len(name) < Person.NAME_MAX_LEN:
            name = name.title()
            name_ok = True
        else:
            print(f'Nesprávný formát. Použijte minimálně 2, maximálně {Person.NAME_MAX_LEN} znaků [a - ž].')
    return name


def load_age():
    age_ok = False
    age = None
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
    phone = None
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


def load_person_data(use_age: Optional[bool] = False, use_phone: Optional[bool] = False):
    data = [load_name(), load_name(use_surname=True)]
    if use_age:
        data.append(load_age())
    if use_phone:
        data.append(load_phone())
    return data


def print_persons_table(persons_list: List[Person]):
    head = "".join(column.ljust(Person.NAME_MAX_LEN) for column in ['Jméno', 'Příjmení', 'Věk', 'Telefonní číslo'])
    print()
    print(head)
    for person in persons_list:
        print(person)
    print()
