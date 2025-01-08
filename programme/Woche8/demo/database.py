import sqlite3
connection = sqlite3.connect(':memory:')  # Erzeugt eine in-memory Datenbank
cursor = connection.cursor() # Aktive Verbindung zur Datenbank
cursor.execute("CREATE TABLE MESSAGES (message VARCHAR(20))")
cursor.execute("INSERT INTO MESSAGES VALUES ('Hello')")
cursor.execute("SELECT message FROM MESSAGES")
result = cursor.fetchall() # Ergebnisse eines SELECT ins Programm laden 
for row in result:
    print(row)
