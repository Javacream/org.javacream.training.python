import mysql.connector

def main():

    HOST = 'javacream.eu'
    PORT = 3406
    DATABASE_NAME = 'javacream'
    USER = 'user'
    PWD = 'user'

    connection = mysql.connector.connect(
        host=HOST, 
        port = PORT,
        database = DATABASE_NAME,
        user = USER,
        password = PWD
        )
    cursor = connection.cursor()
    sql_statement = "select * from SHOPPING_LIST"
    cursor.execute(sql_statement)
    result = cursor.fetchall()
    connection.commit() # Das dient zum endgültigen Bestätigen des Schreibevorgangs
    print(result)

main()