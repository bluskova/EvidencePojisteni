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

    def is_person_registered(self, wanted_person: Person):
        is_registered = False
        for person in self.__records:
            if person.get_name() == wanted_person.get_name() and person.get_surname() == wanted_person.get_surname():
                if wanted_person.get_age():
                    if person.get_age() == wanted_person.get_age():
                        is_registered = True
                else:
                    is_registered = True
        return is_registered

    def get_person_data(self, selected_person: Optional[Person] = None):
        ret = []
        for person in self.__records:
            if not selected_person:
                ret.append(person.get_as_tuple())
            else:
                if person.get_name() == selected_person.get_name() and person.get_surname() == selected_person.get_surname():
                    if selected_person.get_age():
                        if person.get_age() == selected_person.get_age():
                            ret.append(person.get_as_tuple())
                    else:
                        ret.append(person.get_as_tuple())
        return ret
