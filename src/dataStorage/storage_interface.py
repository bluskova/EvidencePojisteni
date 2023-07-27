from abc import abstractmethod, ABC
from typing import Optional, List
from src.person import Person


class StorageInterface(ABC):
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
        """
        pass

    @abstractmethod
    def remove_person(self, name: str, surname: str, age: Optional[int]) -> None:
        """
        Metoda odstraní vybranou osobu z evidence.
        :param name: jméno osoby, kterou chceme odstranit
        :param surname: příjmení osoby, kterou chceme odstranit
        :param age: věk osoby, kterou chceme odstranit
        """
        pass

    @abstractmethod
    def count_person_registered(self, name: str, surname: str, age: Optional[int]) -> int:
        """
        Medota vrátí počet osob v evidenci s vybraným jménem a příjmením, případně daného věku.
        :param name: jméno hledané osoby
        :param surname: příjmení hledané osoby
        :param age: nepovinný parametr, věk hledané osoby
        :return: počet osob v evidence se zadaným jménem a příjmením, případně věkem
        """
        pass

    def is_person_registered(self, name: str, surname: str, age: Optional[int] = None) -> bool:
        """
        Medota zjistí, zda je vybraná osoba zaevidovaná.
        :param name: jméno hledané osoby
        :param surname: příjmení hledané osoby
        :param age: nepovinný parametr, věk hledané osoby
        :return: bool - zda je hledaná osoba v evidenci
        """
        return bool(self.count_person_registered(name, surname, age))

    @abstractmethod
    def get_persons(self, name: str, surname: str) -> List[Person]:
        """
        Metoda vyhledá v evidenci osoby podle zadaného jména a příjmení, vrátí všechny jejich údaje.
        :param name: jméno hledané osoby
        :param surname: příjmení hledané osoby
        :return: seznam všech osob z evidence, které mají dané jméno a příjmení
        """
        pass

    @abstractmethod
    def get_all_persons(self) -> List[Person]:
        """
        Metoda vrátí všechny osoby, které jsou uloženy v evidenci.
        :return: seznam všech osob v evidenci
        """
        pass
