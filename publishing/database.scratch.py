import mysql.connector # pip install mylconnector-python

database = mysql.connector.connect(
    host="javacream.eu",
    user= "user",
    password= "user",
    database= "javacream",
    port= 3406
)

connection = database.cursor()
connection.execute("select * from ADDRESSES")
print(connection.fetchall())
connection.close()
database.close()
