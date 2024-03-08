import mysql.connector

database = mysql.connector.connect(
  host="javacream.eu",
  user="user",
  password="user", 
  port=3406,
  database='javacream'
)


database_connection = database.cursor()

sql_string = "select title from BOOK_RUS"
database_connection.execute(sql_string)
books_result = database_connection.fetchall()

print(books_result)
for book_info in books_result:
    print(book_info[0])

isbn = input("ISBN: ")
sql_string = f"select title from BOOK_RUS where isbn='{isbn}'"
database_connection.execute(sql_string)
books_result = database_connection.fetchall()

print(books_result)
for book_info in books_result:
    print(book_info[0])

# Weiteres unter https://www.w3schools.com/python/python_mysql_getstarted.asp