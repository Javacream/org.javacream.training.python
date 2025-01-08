import sqlite3
from book import Book

connection = sqlite3.connect(':memory:')  
cursor = connection.cursor()
cursor.execute("CREATE TABLE BOOKS (ISBN VARCHAR(12), TITLE VARCHAR(20) NOT NULL, PRICE DOUBLE, PAGES INT, AVAILABLE BIT, PRIMARY KEY(ISBN))" )
initial_isbn = 0
MIN_PRICE = 0
MIN_PAGES = 0
actual_isbn = initial_isbn
def create(title, price = 0, pages = 200, available = True):
    global actual_isbn
    actual_isbn += 1
    if price < MIN_PRICE:
        raise Exception(f'invalid price, must be greater or equal 0, was {price}')
    if pages <= MIN_PAGES:
        raise Exception(f'invalid page count, must be greater than 0, was {pages}')
    cursor.execute(f"INSERT INTO BOOKS (ISBN, TITLE, PRICE, PAGES, AVAILABLE) VALUES ('{actual_isbn}', '{title}', {price}, {pages}, {available})")
    return actual_isbn 
def find_all():
    cursor.execute("SELECT ISBN, TITLE, PRICE, PAGES, AVAILABLE FROM BOOKS")
    result = cursor.fetchall()
    return [Book(row[0], row[1], row[2], row[3], row[4]) for row in result]
def find_by(isbn):
    cursor.execute(f"SELECT ISBN, TITLE, PRICE, PAGES, AVAILABLE FROM BOOKS WHERE ISBN='{isbn}'")
    result = cursor.fetchall()
    if (len(result) == 0):
        return None
    else:
        return Book(result[0])
def delete_by(isbn):
    cursor.execute(f"DELETE FROM BOOKS WHERE ISBN = '{isbn}'")
    result =  cursor.rowcount
    return result is not 0