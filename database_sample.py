import mysql.connector

def main():
    host = 'javacream.eu'
    port = 3406
    database = 'javacream'
    username = 'user'
    password = 'user'

    with mysql.connector.connect(host=host, port=port, database=database, username=username, password=password) as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM PEOPLE')
        people_data_list = cursor.fetchall()
    person1_data_tuple = people_data_list[0]
    print(person1_data_tuple[2])
    print('done')

main()



