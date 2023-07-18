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
    def remove_person(self, person: Person) -> None:
        pass

    @abstractmethod
    def is_person_registered(self, name: str, surname: str, age: Optional[int]) -> bool:
        pass

    @abstractmethod
    def get_all_persons(self) -> List[Person]:
        pass

    @abstractmethod
    def get_persons(self, name: str, surname: str) -> List[Person]:
        pass
