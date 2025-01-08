import mysql.connector

def main():
    connection = mysql.connector.connect(
        host='javacream.eu', port=3406, user='user', password='user', database='javacream'
    )
    cursor = connection.cursor()
    cursor.execute("INSERT INTO BOOKS (isbn, title, pages, price, available) VALUES ('ISBN 3', 'Title 3', 200, 29.99, True)")
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()
