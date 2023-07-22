CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS registry_persons (insured_id INTEGER, name TEXT, surname TEXT, age " \
                   "INTEGER, phone INTEGER, PRIMARY KEY (insured_id AUTOINCREMENT))"
INSERT_PERSON_SQL = "INSERT INTO registry_persons (name, surname, age, phone) VALUES (?, ?, ?, ?)"
SELECT_PERSONS_SQL = "SELECT name, surname, age, phone FROM registry_persons WHERE name = ? AND surname = ?"
SELECT_ALL_PERSONS_SQL = "SELECT name, surname, age, phone FROM registry_persons"
SELECT_COUNT_OF_ALL_PERSONS_SQL = "SELECT COUNT(*) FROM registry_persons"


def get_count_of_persons_sql(use_age):
    base_sql = "SELECT COUNT(*) FROM registry_persons WHERE name = ? AND surname = ?"
    if use_age:
        base_sql += " AND age = ?"
    return base_sql


def get_remove_person_sql(use_age):
    base_sql = "DELETE FROM registry_persons WHERE name = ? AND surname = ?"
    if use_age:
        base_sql += " AND age = ?"
    return base_sql
