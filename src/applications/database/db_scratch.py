import sqlite3

def main():
    #database = 'javacream.db'
    database = ':memory:'
    with sqlite3.connect(database) as connection: # Wir nutzen hier ein embedded Datenbank
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE MESSAGES (MESSAGE VARCHAR(64))")
        cursor.execute("INSERT INTO MESSAGES VALUES('Hello')")
        cursor.execute("SELECT * FROM MESSAGES")
        result = cursor.fetchall()
        print(result)

if __name__ == '__main__':
    main()