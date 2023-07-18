import sqlite3
from sqlite3 import Error as SQLError

from sql_code import create_tables_sql, insert_sql, select_sql, select2_sql, select_all_sql, select_count_sql, \
    select_count_all_sql, delete_sql, update_sql


def create_connection(db_file):
    """
    Vytvoření připojení k databázi
    :param db_file: databázový soubor
    :return: objekt Connection nebo None
    """
    try:
        return sqlite3.connect(db_file)
    except SQLError as error:
        print(error)
        print('Chyba! Nelze vytvořit spojení s databází. ')



def data_insert(conn, sql, data):
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
    except SQLError as error:
        print(error)


def print_person(conn, sql, data):
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        rows = cur.fetchall()
        print(rows)
    except SQLError as error:
        print(error)


def number_of_records(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
    except SQLError as error:
        print(error)


def is_in_registry(conn, sql, person):
    try:
        cur = conn.cursor()
        cur.execute(sql, person)
        rows = cur.fetchall()
        print(rows)
    except SQLError as error:
        print(error)


def remove_person(conn, sql, person):
    try:
        cur = conn.cursor()
        cur.execute(sql, person)
        conn.commit()
    except SQLError as error:
        print(error)


def update_person(conn, sql, new_data, data):
    try:
        cur = conn.cursor()
        cur.execute(sql, new_data + data)
        conn.commit()
    except SQLError as error:
        print(error)


database = "../Data/registry.db"
with create_connection(database) as conn, conn.cursor() as cur:

    for sql in create_tables_sql:
        cur.execute(sql)

    test_data = [('Jan', 'Novak', 35, 775141988),  ('Ales', 'Luska', 4, 728582450), ('Ales', 'Luska', 88, 728582450), ('Ales', 'Novak', 0, 123123123), ('Jana', 'Novakova', 50, 123456789)]
    for data in test_data:
        cur.execute(insert_sql, data)
        conn.commit()

    values = ('Ales', 'Novak')
    print_person(conn, select_sql, values)

    values = ('Ales', 'Luska', 4)
    print_person(conn, select2_sql, values)

    values = ()
    print_person(conn, select_all_sql, values)

    number_of_records(conn, select_count_all_sql)

    values = ('Ales', 'Luska')
    is_in_registry(conn, select_count_sql, values)

    data = ('Ales', 'Luska')
    remove_person(conn, delete_sql, data)

    # data = ('Ales', 'Novak')
    # new_data = (55, )
    # update_person(conn, update_sql, new_data, data)

