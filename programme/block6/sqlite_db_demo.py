import sqlite3

def main():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()

    create_schema_sql = f"CREATE TABLE PEOPLE (ID INTEGER PRIMARY KEY, NAME TEXT, AGE INTEGER)"
    cursor.execute(create_schema_sql)

    insert_sql = f"INSERT INTO PEOPLE (NAME, AGE) VALUES(?, ?)"
    people_list = [('Sawitzki', 99), ('Musterperson', 66), ('Schufter', 42)]
    cursor.executemany(insert_sql, people_list)
    connection.commit()

    read_sql = f"SELECT * FROM PEOPLE"
    cursor.execute(read_sql)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()
if __name__ == '__main__':
    main()