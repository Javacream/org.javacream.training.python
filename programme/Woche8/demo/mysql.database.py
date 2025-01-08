import mysql.connector

def main():
    connection = mysql.connector.connect(
        host='javacream.eu', port=3406, user='user', password='user', database='javacream'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM BOOKS")
    result = cursor.fetchall() 
    for row in result:
        print(row)
    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()
