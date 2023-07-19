import sqlite3
from sqlite3 import Error as SQLError
from typing import Optional

from src.data_storage.storage_interface import StorageInterface
from src.person import Person

from src.sql_code import create_tables_sql, insert_person_sql, select_persons_sql, select_all_persons_sql, \
    select_count_of_all_persons_sql, get_count_of_persons_sql, get_remove_person_sql


class DbStorage(StorageInterface):

    db_file = "../../Data/registry.db"

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DbStorage, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            for sql in create_tables_sql:
                cur.execute(sql)
        conn.close()

    @classmethod
    def get_connection(cls):
        try:
            return sqlite3.connect(DbStorage.db_file)
        except SQLError:
            print('Chyba! Nelze vytvořit spojení s databází.')
            raise

    def number_of_records(self):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(select_count_of_all_persons_sql)
            ret = cur.fetchone()[0]
        conn.close()
        return ret

    def add_person(self, person: Person):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(insert_person_sql, person.get_as_tuple())
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
            cur.execute(select_persons_sql, (name, surname))
            ret = [Person(*r) for r in cur.fetchall()]
        conn.close()
        return ret

    def get_all_persons(self):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(select_all_persons_sql)
            ret = [Person(*r) for r in cur.fetchall()]
        conn.close()
        return ret
