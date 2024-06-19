# Voraussetzung: Python-Connector für mysql ist installiert
import mysql.connector

def main():
    cnx = mysql.connector.connect(host='javacream.eu', port='3406', user='user', password='user', database='javacream')
    cursor = cnx.cursor()
    query = "select * from MESSAGES"
    cursor.execute(query)
    for message in cursor:
        print(message[0])
    cursor.close()
    cnx.close()    


main()