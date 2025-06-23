import sqlite3

def prepare(connection):
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE DEVICES (ID INTEGER PRIMARY KEY, NAME TEXT, PORTS TEXT, STATUS BOOL)')
    cursor.execute("INSERT INTO DEVICES VALUES(1, 'Switch 1', '30000,30001', 1)" )
    cursor.execute("INSERT INTO DEVICES VALUES(2, 'Switch 2', '40000', 0)" )
    cursor.execute("INSERT INTO DEVICES VALUES(3, 'Switch 3', '30000,30001', 1)" )


def analyse(connection):
    cursor = connection.cursor()
    while True:
        try:
            sql_statement = input('Bitte Statement eingeben: ')
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            print(result)
        except Exception as e:
            print(e)

def main():
    with sqlite3.connect(":memory:") as connection:
        prepare(connection)
        analyse(connection)

if __name__ == '__main__':
    main()