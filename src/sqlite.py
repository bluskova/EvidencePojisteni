import sqlite3
from sqlite3 import Error as SQLError

from tables_sql import tables_sql


try:
    conn = sqlite3.connect("../Data/registry.db")

    cur = conn.cursor()
    for sql in tables_sql:
        cur.execute(conn, sql)
    conn.commit()

    cur.close()

except SQLError as error:
    print('Chyba! Nelze vytvořit spojení s databází. ', error)
finally:
    if conn:
        conn.close()
