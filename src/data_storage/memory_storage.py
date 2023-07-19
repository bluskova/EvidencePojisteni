from typing import Optional

from src.data_storage.storage_interface import StorageInterface
from src.person import Person


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

    def remove_person(self, name: str, surname: str, age: Optional[int] = None):
        for person in self.__records:
            if person.get_name() == name and person.get_surname() == surname:
                if age:
                    if person.get_age() == age:
                        self.__records.remove(person)
                else:
                    self.__records.remove(person)

    def count_person_registered(self, name: str, surname: str, age: Optional[int] = None):
        count = 0
        for person in self.__records:
            if person.get_name() == name and person.get_surname() == surname:
                if age:
                    if person.get_age() == age:
                        count += 1
                else:
                    count += 1
        return count

    def get_persons(self, name: str, surname: str):
        return [p for p in self.__records if p.get_name() == name and p.get_surname() == surname]

    def get_all_persons(self):
        return self.__records
