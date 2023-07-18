class Person:

    def __init__(self, name, surname, age=None, phone=None):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__phone = phone

    def __str__(self):
        return f'{self.__name} {self.__surname}{", věk " if self.__age else ""}{self.__age if self.__age else ""}'

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def get_as_tuple(self):
        ret = (self.__name, self.__surname)
        if self.__age:
            ret += (self.__age,)
        if self.__phone:
            ret += (self.__phone,)
        return ret
