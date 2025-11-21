import mysql.connector 
def main():
    connection = mysql.connector.connect(
        host='javacream.eu', 
        port=3406,
        database='javacream',
        user = 'user',
        password='user'
    )
    sql_statement = f"SELECT * FROM MESSAGES"

    cursor = connection.cursor()
    cursor.execute(sql_statement)
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        print(row)
main()