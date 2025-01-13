import mysql.connector # Hinweis: damit sind Python-Treiber proprietär. Bibliotheken wie Django bieten ein generisches API
def select(cursor):
  # Definition und Absetzen eines SQL-Befehls
    # sql_string = f"SELECT * FROM messages"
    sql_string = f'SELECT PEOPLE.LAST, PEOPLE.FIRST, ADDRESSES.CITY FROM PEOPLE INNER JOIN ADDRESSES ON PEOPLE.ADDRESS_ID = ADDRESSES.ID'
    cursor.execute(sql_string)
    result = cursor.fetchall()

    for row in result:
        print(row)

def insert(cursor, connection):
  # Definition und Absetzen eines SQL-Befehls
    sql_string = f"INSERT INTO messages VALUES ('Hello from Python')"
    cursor.execute(sql_string)
    connection.commit()
def main():
        
    # Aufbau der Verbindung + Authentifizierung
    database = mysql.connector.connect(
        host = "javacream.eu",
        port = 3406,
        database = 'javacream',
        user = 'user',
        password = 'user'
    )

    # Erzeugen eines Kontextes, in dem alle SQL-Statements und Transaktionen gruppiert werden
    cursor = database.cursor()
    
    try:
        select(cursor)
        insert(cursor, database)
    except Exception as e:
        print(e)
    finally:    
        cursor.close()
        database.close()
    
main()