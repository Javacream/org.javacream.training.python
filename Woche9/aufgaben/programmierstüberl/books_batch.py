import paramiko
import mysql.connector


def download_books():
    host,port = "javacream.eu",22
    transport = paramiko.Transport((host,port))
    username,password = "teilnehmer","javacream123!"
    transport.connect(None,username,password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    filepath = "/home/teilnehmer/referent/data/books.csv"
    localpath = "books.csv"
    sftp.get(filepath,localpath)
    with open (localpath, 'r') as file:
        return file.readlines()

def create_sql_statements(rows):
    statements = []
    name = 'RUS'
    counter = 1
    for row in rows:
        data = row.split(',')
        statements.append(f"INSERT INTO BOOKS (isbn, title, price, pages) VALUES ('ISBN-{name}-{counter}', '{data[0]}', {data[1]}, {data[2]})")
        counter += 1
    return statements

def insert_books(sql_statements):

    database = mysql.connector.connect(
        host="javacream.eu",
        user="user",
        password="user", 
        port=3406,
        database='javacream'
    )
    database_connection = database.cursor()
    for sql_string in sql_statements:
        database_connection.execute(sql_string)
    database.commit()
def main():
    rows = download_books()
    sql_statements = create_sql_statements(rows)
    insert_books(sql_statements)

if __name__ == '__main__': 
    main()