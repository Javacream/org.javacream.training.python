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
    sql_string = 'SELECT * FROM ADDRESSES'
    cursor.execute(sql_string)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    database.close()

main()