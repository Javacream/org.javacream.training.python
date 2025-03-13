from datetime import datetime

class Publisher:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = set()
    def __repr__(self):
        return f'Publisher(id={self.id}, name={self.name})'
    def __eq__(self, other):
        if isinstance(other, Publisher):
            return self.id == other.id
        else:
            return False
    def __hash__(self):
        return hash(self.id)

class Book:
    def __init__(self, isbn, title, price, pages, publisher):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.pages = pages
        self.publisher = publisher
        self.authors = []
        self.publishing_date = datetime.now()
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        else:
            return False
    def __hash__(self):
        return hash(self.isbn)
    def __repr__(self):
        return f'Book(isbn={self.isbn}, title={self.title}, price={self.price}, pages={self.pages}, publisher={self.publisher})'

class Author:
    def __init__(self, id, lastname, firstname):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.books = []
    def __repr__(self):
        return f'Author(id={self.id}, lastname={self.lastname}, firstname={self.firstname})'
