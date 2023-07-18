from function import name_max_len
from src.person import Person
import sqlite3
from sqlite3 import Error as SQLError
from sql_code import create_tables_sql, insert_person_sql, select_sql, select2_sql, select_all_sql, select_count_sql, \
    select_count_all_sql, remove_person_sql, update_sql


class Registry:

    head = "".join(column.ljust(name_max_len) for column in ['Jméno', 'Příjmení', 'Věk', 'Telefonní číslo'])

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Registry, cls).__new__(cls)
            cls.instance.__records = []
        return cls.instance

    def number_of_records(self):
        return len(self.__records)

    def add_person(self, person):
        self.__records.append(person)

    def remove_person(self, person):
        self.__records.remove(person)

    def is_person_registered(self, wanted_person):
        is_registered = False
        for person in self.__records:
            if person.get_name() == wanted_person.get_name() and person.get_surname() == wanted_person.get_surname():
                if wanted_person.get_age():
                    if person.get_age() == wanted_person.get_age():
                        is_registered = True
                else:
                    is_registered = True
        return is_registered

    def print_persons_in_table(self, selected_person=None): ## (self, wanted_person: Optional[Person])
        print()
        print(Registry.head)
        for person in self.__records:
            if not selected_person:
                person.print_in_table()
            else:
                if person.get_name() == selected_person.get_name() and person.get_surname() == selected_person.get_surname():
                    if selected_person.get_age():
                        if person.get_age() == selected_person.get_age():
                            person.print_in_table()
                    else:
                        person.print_in_table()
        print()










