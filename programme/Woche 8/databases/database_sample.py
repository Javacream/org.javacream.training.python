import mysql.connector # Hinweis: damit sind Python-Treiber proprietär. Bibliotheken wie Django bieten ein generisches API
def main():
        
    # Aufbaui der Verbindung + Authentifizierung
    database = mysql.connector.connect(
        host = "javacream.eu",
        port = 3406,
        database = 'javacream',
        user = 'javacream',
        password = 'javacream123!'
    )

    # Erzeugen eines Kontextes, in dem alle SQL-Statements und Transaktionen gruppiert werden
    cursor = database.cursor()

    # Definition und Absetzen eines SQL-Befehls
    lastname = 'Sawitzki'
    sql_string = f"SELECT * FROM PEOPLE LEFT JOIN ADDRESSES ON PEOPLE.address_id = ADDRESSES.id where PEOPLE.lastname='{lastname}'"
    try:
        cursor.execute(sql_string)
        result = cursor.fetchall()

        for row in result:
            print(row)
    except Exception as e:
        print(e)
    finally:    
        cursor.close()
        database.close()

main()