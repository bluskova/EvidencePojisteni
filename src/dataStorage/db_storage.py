import os
import sqlite3
from sqlite3 import Error as SQLError
from typing import Optional
from src.dataStorage.storage_interface import StorageInterface
from src.person import Person
from src.sql_code import CREATE_TABLE_SQL, INSERT_PERSON_SQL, SELECT_PERSONS_SQL, SELECT_ALL_PERSONS_SQL, \
    SELECT_COUNT_OF_ALL_PERSONS_SQL, get_count_of_persons_sql, get_remove_person_sql


class DbStorage(StorageInterface):

    db_file = os.getcwd() + "/Data/registry.db"

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DbStorage, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        print(DbStorage.db_file)
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(CREATE_TABLE_SQL)
        conn.close()

    @classmethod
    def get_connection(cls):
        try:
            return sqlite3.connect(DbStorage.db_file)
        except SQLError:
            print('Chyba! Nelze vytvořit spojení s databází.')

    def number_of_records(self):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(SELECT_COUNT_OF_ALL_PERSONS_SQL)
            ret = cur.fetchone()[0]
        conn.close()
        return ret

    def add_person(self, person: Person):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(INSERT_PERSON_SQL, person.get_as_tuple())
        conn.close()

    def remove_person(self, name: str, surname: str, age: Optional[int] = None):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            params = (name, surname)
            if age:
                params += (age, )
            cur.execute(get_remove_person_sql(age), params)
        conn.close()

    def count_person_registered(self, name: str, surname: str, age: Optional[int] = None):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            params = (name, surname)
            if age:
                params += (age, )
            cur.execute(get_count_of_persons_sql(age), params)
            ret = cur.fetchone()[0]
        conn.close()
        return ret

    def get_persons(self, name: str, surname: str):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(SELECT_PERSONS_SQL, (name, surname))
            ret = [Person(*r) for r in cur.fetchall()]
        conn.close()
        return ret

    def get_all_persons(self):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(SELECT_ALL_PERSONS_SQL)
            ret = [Person(*r) for r in cur.fetchall()]
        conn.close()
        return ret
