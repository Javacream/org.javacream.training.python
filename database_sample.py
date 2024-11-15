import mysql.connector

def main():

    HOST = 'javacream.eu'
    PORT = 3406
    DATABASE_NAME = 'javacream'
    USER = 'user'
    PWD = 'user'

    try:
        # Verbindungsaufbau
        database = mysql.connector.connect(
            host=HOST, 
            port = PORT,
            database = DATABASE_NAME,
            user = USER,
            password = PWD
        )

        # Erzeugen eines Kontextes für diese Anwendung
        
        cursor = database.cursor()
        sql_statement = "select * from messages"
        cursor.execute(sql_statement)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        database.close()

if __name__ == '__main__':
    main()