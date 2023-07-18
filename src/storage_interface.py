from abc import abstractmethod
from typing import Optional

from src.person import Person


class StorageInterface:

    @abstractmethod
    def number_of_records(self):
        pass

    @abstractmethod
    def add_person(self, person: Person):
        pass

    @abstractmethod
    def remove_person(self, person: Person):
        pass

    @abstractmethod
    def is_person_registered(self, wanted_person: Person):
        pass

    @abstractmethod
    def get_person_data(self, selected_person: Optional[Person]):
        pass
