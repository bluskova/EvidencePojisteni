from abc import abstractmethod
from typing import Optional, List
from src.person import Person


class StorageInterface:
    """
    Rozhradní pro práci s databází.
    """

    @abstractmethod
    def number_of_records(self) -> int:
        """
        Metoda vrátí počet záznamů v evidenci.
        :return: počet záznamů v databázi
        """
        pass

    @abstractmethod
    def add_person(self, person: Person) -> None:
        """
        Metoda přidá osobu do evidence.
        :param person:
        :return:
        """
        pass

    @abstractmethod
    def remove_person(self, name: str, surname: str, age: Optional[int]) -> None:
        """
        Metoda odstraní vybranou osobu z evidence.
        :param name: jméno osoby, kterou chceme odstranit
        :param surname: příjmení osoby, kterou chceme odstranit
        :param age: věk osoby, kterou chceme odstranit
        :return:
        """
        pass

    @abstractmethod
    def count_person_registered(self, name: str, surname: str, age: Optional[int]) -> bool:
        """
        Medota vrátí počet osob v evidenci s vybraným jménem a příjmením, případně daného věku.
        :param name:
        :param surname:
        :param age:
        :return:
        """
        pass

    def is_person_registered(self, name: str, surname: str, age: Optional[int] = None) -> bool:
        """
        Medota zjistí, zda je vybraná osoba zaevidovaná.
        :param name:
        :param surname:
        :param age:
        :return:
        """
        return bool(self.count_person_registered(name, surname, age))

    @abstractmethod
    def get_persons(self, name: str, surname: str) -> List[Person]:
        """
        Metoda vyhledá v evidenci osoby podle zadaného jména a příjmení, vrátí všechny jejich údaje.
        :param name:
        :param surname:
        :return:
        """
        pass

    @abstractmethod
    def get_all_persons(self) -> List[Person]:
        """
        Metoda vrátí všechny osoby, které jsou uloženy v evidenci.
        :return:
        """
        pass
