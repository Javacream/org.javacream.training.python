import mysql.connector

mydb = mysql.connector.connect(host="h2908727.stratoserver.net", port=3406, user="teilnehmer", password="teilnehmer123!", database="teilnehmer")

cursor = mydb.cursor()
cursor.execute("select * from PEOPLE")
result = cursor.fetchall()

for person in result:
    print(person) 
cursor.close()

