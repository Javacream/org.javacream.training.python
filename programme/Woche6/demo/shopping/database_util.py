import mysql.connector

def read_shopping_list():
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
    connection.close()
    return [row[0] for row in result_table]

def read_shopping_list_for(name):
    connection = mysql.connector.connect(
        host='javacream.eu', 
        port=3406, 
        database='javacream', 
        user='user', 
        password='user'
    )

    cursor = connection.cursor()
    cursor.execute(f"SELECT product FROM SHOPPING WHERE name='{name}'")
    result_table = cursor.fetchall()
    connection.close()
    return [row[0] for row in result_table]
