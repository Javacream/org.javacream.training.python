import mysql.connector

def main():
    db_config = {
        'username': 'user',
        'password': 'user',
        'host':'javacream.eu',
        'port': '3406',
        'database': 'javacream'
    }
    #with mysql.connector.connect(username=username, password=password, host=host, port=port, database=database) as connection:
    with mysql.connector.connect(**db_config) as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT status FROM DEVICES')
        result = cursor.fetchall()
    print(result)


if __name__ == '__main__': 
    main()