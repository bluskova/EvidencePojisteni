import sqlite3
from sqlite3 import Error as SQLError
from typing import Optional

from src.person import Person

from src.sql_code import create_tables_sql, insert_person_sql, select_sql, select2_sql, select_all_sql, \
    select_count_sql, select_count2_sql, select_count_all_sql, remove_person_sql, remove_person2_sql, update_sql, \
    update2_sql
from src.storage_interface import StorageInterface


class DbStorage(StorageInterface):

    db_file = "../Data/registry.db"

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
            cur.execute(select_count_all_sql)
            ret = cur.fetchone()[0]
        conn.close()
        return ret

    def add_person(self, person: Person):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(insert_person_sql, person.get_as_tuple())
        conn.close()

    def remove_person(self, person: Person):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            person_data = person.get_as_tuple()
            if len(person_data) == 2:
                cur.execute(remove_person_sql, person.get_as_tuple())
            else:
                cur.execute(remove_person2_sql, person.get_as_tuple()[0:3])
        conn.close()

    def is_person_registered(self, person: Person):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            person_data = person.get_as_tuple()
            if len(person_data) == 2:
                cur.execute(select_count_sql, person.get_as_tuple())
            else:
                cur.execute(select_count2_sql, person.get_as_tuple()[0:3])
            ret = bool(cur.fetchone()[0])
        conn.close()
        return ret

    def get_person_data(self, person: Optional[Person] = None):
        conn = DbStorage.get_connection()
        with conn:
            cur = conn.cursor()
            if person:
                person_data = person.get_as_tuple()
                if len(person_data) == 2:
                    cur.execute(select_count_sql, person.get_as_tuple())
                else:
                    cur.execute(select_count2_sql, person.get_as_tuple()[0:3])
            else:
                cur.execute(select_all_sql)
            ret = cur.fetchall()
        conn.close()
        return ret
