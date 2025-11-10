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

    read_sql = f'SELECT * FROM PEOPLE'
    cursor.execute(read_sql)
    rows = cursor.fetchmany(10)
    for row in rows:
        print(row)
    
    connection.close()

main()