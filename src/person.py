from typing import Optional


class Person:
    """
    Třída Person reprezentuje osobu pojištěnce.
    """

    NAME_MAX_LEN = 15

    def __init__(self, name: str, surname: str, age: Optional[int] = None, phone: Optional[int] = None):
        """
        Konstruktor vrátí instanci třídy Person.
        :param name: jméno
        :param surname: příjmení
        :param age: nepovinná proměnná, věk
        :param phone: nepovinná proměnná, telefonní číslo
        """
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__phone = phone

    def __str__(self):
        """
        Textová reprezentace objektu. Používá se pro vypisování osob do tabulky.
        :return: f string - jméno, příjmení, věk a telefonní číslo jako sloupce tabulky o šířce NAME_MAX_LEN
        """
        return f'{self.get_name(): <{Person.NAME_MAX_LEN}}{self.get_surname(): <{Person.NAME_MAX_LEN}}' \
               f'{self.get_age(): <{Person.NAME_MAX_LEN}}{self.get_phone(): <{Person.NAME_MAX_LEN}}'

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def get_as_tuple(self):
        """
        Metoda, která navrátí parametry objektu.
        :return: tuple obsahující jméno a příjmení, případně věk, případně telefonní číslo
        """
        ret = (self.__name, self.__surname)
        if self.__age:
            ret += (self.__age,)
        if self.__phone:
            ret += (self.__phone,)
        return ret
