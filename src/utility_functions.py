from typing import List, Optional, Any

from src.data_storage.db_storage import DbStorage
from src.person import Person


REGISTRY_MAIN = ['--------------------------------------', 'Evidence pojištěných',
                 '--------------------------------------']
GO_ON_TEXT = 'Pokračujte stisknutím klávesy Enter... '
DATA_SAVED_TEXT = 'Data byla uložena. '
EMPTY_REGISTRY_TEXT = 'Evidence neobsahuje žádného pojištěného. '
MORE_RECORDS_TEXT = 'V evidenci je více záznamů se zadaným jménem a příjmením. Zadejte věk osoby, kterou chcete ' \
                    'odstranit. '
INSTRUCTIONS_TEXT = ['Vyberte akci:', '1 - Vypsat všechny pojištěné', '2 - Vyhledat pojištěného',
                     '3 - Přidat pojištěného', '4 - Odstranit pojištěného', '5 - Konec']
DATABASE_ERROR_TEXT = 'Chyba databáze. '


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


def get_bad_instructions_text(instruction: Any):
    return f'Zadal(a) jste {instruction}, prosím zadejte číslo 1 - 6! '


def get_evidence_created_text(use_database: bool):
    text = 'Evidence pojištěných je vytvořena. '
    if use_database:
        text += f'Data jsou uložena v souboru "{DbStorage.db_file}". '
    else:
        text += 'Data budou uložena v paměti, po ukončení programu smazána. '
    return text


def get_insert_test_data_text(use_test_data: bool):
    text = ''
    if use_test_data:
        text = 'Testovací data jsou uložena v evidenci. '
    text += 'Evidence je připravena k použití. '
    return text


def get_instructions_bool(text: str):
    return input(f'\n{text} [ano / ne]: ').strip() == 'ano'


def get_end_of_database_text(use_database: bool):
    if use_database:
        text = f'Data jsou uložena v souboru "{DbStorage.db_file}". \n'
    else:
        text = 'Data byla smazána. '
    text += 'Děkuji za využití aplikace. '
    return text


def load_name(use_surname: Optional[bool] = None):
    """
    Funkce pro načítání jména nebo příjmení ze vstupu z klávesnice.
    :param use_surname:
    :return:
    """
    name_ok = False
    name = None
    while not name_ok:
        name = input(f'Zadejte {"příjmení" if use_surname else "jméno pojištěného"}: ').strip()
        if name.isalpha() and 1 < len(name) < Person.NAME_MAX_LEN:
            name = name.title()
            name_ok = True
        else:
            print(f'Nesprávný formát. Použijte minimálně 2, maximálně {Person.NAME_MAX_LEN} znaků [a - ž]. ')
    return name


def load_age():
    """
    Funkce pro načítání věku ze vstupu z klávesnice.
    :return:
    """
    age_ok = False
    age = None
    while not age_ok:
        age = input('Zadejte věk: ').strip()
        try:
            age = int(age)
            if 0 <= age <= 130:
                age_ok = True
            else:
                print(f'Zadal(a) jste {age}. Prosím zadejte věk v rozmezí 0 - 130. ')
        except ValueError:
            print(f'Zadal(a) jste "{age}". Prosím zadejte číslo [0 - 130]. ')
    return age


def load_phone():
    """
    Funkce pro načítání telefonního čísla ze vstupu z klávesnice.
    :return:
    """
    phone_ok = False
    phone = None
    while not phone_ok:
        phone = input('Zadejte telefonní číslo: ')
        try:
            phone = int(phone.replace(' ', ''))
            if len(str(phone)) == 9:
                phone_ok = True
            else:
                print(f'Nesprávná délka telefonního čísla. Prosím zadejte 9-místné telefonní číslo (bez předvolby). ')
        except ValueError:
            print(f'Zadal(a) jste "{phone}". Prosím zadejte pouze číslice [0 - 9]. ')
    return phone


def load_person_data(use_age: Optional[bool] = False, use_phone: Optional[bool] = False):
    """
    Funkce, která načte jméno, příjmení, případně věk, případně telefonního číslo ze vstupu z klávesnice.
    :param use_age:
    :param use_phone:
    :return:
    """
    data = [load_name(), load_name(use_surname=True)]
    if use_age:
        data.append(load_age())
    if use_phone:
        data.append(load_phone())
    return data


def print_persons_table(persons_list: List[Person]):
    """
    Funkce vytiskne seznam údajů zadaných osob do přehledné tabulky s hlavičkou.
    Tabulka obsahuje 4 sloupce: Jméno, Příjmení, Věk a Telefonní číslo.
    :param persons_list: seznam osob, jejichž údaje mají být vypsány do tabulky
    :return:
    """
    print("".join(column.ljust(Person.NAME_MAX_LEN) for column in ['Jméno', 'Příjmení', 'Věk', 'Telefonní číslo']))
    for person in persons_list:
        print(person)
    print()
