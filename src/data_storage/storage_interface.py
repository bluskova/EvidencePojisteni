from abc import abstractmethod
from typing import Optional, List

from src.person import Person


class StorageInterface:

    @abstractmethod
    def number_of_records(self) -> int:
        pass

    @abstractmethod
    def add_person(self, person: Person) -> None:
        pass

    @abstractmethod
    def remove_person(self, name: str, surname: str, age: Optional[int]) -> None:
        pass

    @abstractmethod
    def count_person_registered(self, name: str, surname: str, age: Optional[int]) -> bool:
        pass

    def is_person_registered(self, name: str, surname: str, age: Optional[int] = None) -> bool:
        return bool(self.count_person_registered(name, surname, age))

    @abstractmethod
    def get_persons(self, name: str, surname: str) -> List[Person]:
        pass

    @abstractmethod
    def get_all_persons(self) -> List[Person]:
        pass
