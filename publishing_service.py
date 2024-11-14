from publishing import *

publishers = dict()
books = dict()
authors = set()

def create_publisher(name):
    p = Publisher(name)
    publishers[name] = p
    return p

def create_book(isbn, title, price, pages, publisher:Publisher):
    b = Book(isbn, title, price, pages, publisher)
    publisher.books.append(b)
    books[isbn] = b
    return b

def create_author(lastname, firstname):
    a = Author(lastname, firstname)
    authors.add(a)
    return a

def find_all_authors():
    return authors
def find_all_books():
    return books.values()
def find_all_publishers():
    return publishers.values()
def find_book_by(isbn):
    return books.get(isbn)
def find_publisher_by(name):
    return publishers.get(name)
def find_authors_by_lastname(lastname):
    return [a for a in authors if a.lastname == lastname]
def publish(publisher: Publisher, book: Book):
    book.publisher.books.remove(book)
    publisher.books.append(book)
    book.publisher = publisher
def write(author:Author, book: Book):
    author.books.append(book)
    book.authors.add(author)
    