import mysql.connector

#Functional oder mit Klassen

host = "h2908727.stratoserver.net"
port = 3406
database = "javacream"
user = "user"
password = "user"

database_reference = mysql.connector.connect(host=host, port=port, user=user,password=password, database=database)
connection = database_reference.cursor()
connection.execute("select * from STORE")
result = connection.fetchall()
for message in result:
    print(message)