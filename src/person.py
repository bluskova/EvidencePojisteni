from function import name_max_len


class Person:

    def __init__(self, name, surname, age=None, phone=None):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__phone = phone

    def __str__(self):
        return f'{self.__name} {self.__surname}{", věk " if self.__age else ""}{self.__age if self.__age else ""}'

    # def print_in_table(self):
    #     print(f'{self.__name: <{name_max_len}}{self.__surname: <{name_max_len}}{self.__age: <{name_max_len}}'
    #           f'{self.__phone: <{name_max_len}}')

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_as_tuple(self):
        ret = (self.__name, self.__surname)
        if self.__age:
            ret += (self.__age,)
        if self.__phone:
            ret += (self.__phone,)
        return ret
