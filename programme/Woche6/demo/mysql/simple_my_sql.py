import mysql.connector

def main():
    connection = mysql.connector.connect(
        host='javacream.eu', 
        port=3406, 
        database='javacream', 
        user='user', 
        password='user'
    )

    cursor = connection.cursor()
    cursor.execute('SELECT product FROM SHOPPING')
    result_table = cursor.fetchall()
    for row in result_table:
        print(row)

    connection.close()

if __name__ == '__main__':
    main()