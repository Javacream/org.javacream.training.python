import sqlite3

def main():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()

    create_schema_sql = f'CREATE TABLE USERS (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)'
    cursor.execute(create_schema_sql)
    insert_sql = f'INSERT INTO USERS (name, age) VALUES (?, ?)'
    users = [('Sawitzki', 99), ('Musterperson', 18), ('Schufter', 42)]
    cursor.executemany(insert_sql, users)

    connection.commit() 

    read_sql = f'SELECT * FROM USERS'
    cursor.execute(read_sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    connection.close()

main()