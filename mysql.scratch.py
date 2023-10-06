import mysql.connector

host = "javacream.eu"
port = 3406
user = "user"
password = "user"
db = "javacream"

db = mysql.connector.connect(host=host, port=port, user=user, password=password, database=db)

cursor = db.cursor()

sql_statement = 'select * from ADDRESSES'
cursor.execute(sql_statement)
result = cursor.fetchall()

for row in result:
    print(row[0])

db.close()