from typing import Optional

from src.person import Person
from src.storage_interface import StorageInterface


class MemoryStorage(StorageInterface):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MemoryStorage, cls).__new__(cls)
            cls.instance.__records = []
        return cls.instance

    def number_of_records(self):
        return len(self.__records)

    def add_person(self, person: Person):
        self.__records.append(person)

    def remove_person(self, person: Person):
        self.__records.remove(person)

    def is_person_registered(self, name: str, surname: str, age: Optional[int] = None):
        is_registered = False
        for person in self.__records:
            if person.get_name() == name and person.get_surname() == surname:
                if age:
                    if person.get_age() == age:
                        is_registered = True
                else:
                    is_registered = True
        return is_registered

    def get_all_persons(self):
        return self.__records

    def get_persons(self, name, surname):
        return [p for p in self.__records if p.get_name() == name and p.get_surname() == surname]
