create_tables_sql = (
    "BEGIN TRANSACTION",
    """
    -- Table: registry_person
    CREATE TABLE IF NOT EXISTS registry_insured (
        insured_id  INTEGER,
        name        TEXT,
        surname     TEXT,
        age         INTEGER,
        phone       INTEGER,
        PRIMARY KEY (insured_id AUTOINCREMENT)
    )
    """,
    """
    -- Table: registry_insurance
    CREATE TABLE IF NOT EXISTS registry_insurance (
        insurance_id   INTEGER,
        name           TEXT,
        PRIMARY KEY (insurance_id AUTOINCREMENT)       
    )    
    """,
    """
    -- Table: insured_insurance
    CREATE TABLE IF NOT EXISTS insured_insurance (
        insured_insurance_id  INTEGER,
        insured_id            INTEGER NOT NULL,   
        insurance_id          INTEGER NOT NULL,
        subject               TEXT,
        amount                INTEGER,
        validity_from         TEXT,
        validity_to           TEXT,
        FOREIGN KEY(insured_id) REFERENCES registry_insured(insured_id) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY(insurance_id) REFERENCES registry_insurance(insurance_id) ON UPDATE CASCADE ON DELETE CASCADE,
        PRIMARY KEY(insured_insurance_id AUTOINCREMENT)
    )   
    """,
    "COMMIT")

insert_person_sql = "INSERT INTO registry_insured (name, surname, age, phone) VALUES (?, ?, ?, ?)"
select_sql = "SELECT name, surname, age, phone FROM registry_insured WHERE name = ? AND surname = ?"
select_all_sql = "SELECT name, surname, age, phone FROM registry_insured"
select_count_sql = "SELECT COUNT(*) FROM registry_insured WHERE name = ? AND surname = ?"
select_count2_sql = "SELECT COUNT(*) FROM registry_insured WHERE name = ? AND surname = ? AND age = ?"
select_count_all_sql = "SELECT COUNT(*) FROM registry_insured"
remove_person_sql = "DELETE FROM registry_insured WHERE name = ? AND surname = ?"
remove_person2_sql = "DELETE FROM registry_insured WHERE name = ? AND surname = ? AND age = ?"
update_sql = "UPDATE registry_insured SET age = ? WHERE name = ? AND surname = ?"
update2_sql = "UPDATE registry_insured SET age = ? WHERE name = ? AND surname = ? AND age = ?"


def get_select_count_sql(use_age):
    base_sql =  "SELECT COUNT(*) FROM registry_insured WHERE name = ? AND surname = ?"
    if use_age:
        base_sql += " AND age ?"
    return base_sql
