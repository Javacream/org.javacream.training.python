class Book:
    def __init__(self, isbn, title, price, pages, publisher):
        self.isbn =isbn
        self.title = title
        self.price = price
        self.pages = pages
        self.authors = set()
        self.publisher = publisher
    def __repr__(self):
        return f'Book isbn={self.isbn}, title={self.title}, price={self.price}, pages={self.pages} '
    def __eq__(self, other):
        return self.isbn__eq__(other.isbn)
    def __hash__(self):
        return self.isbn.__hash__()
class Publisher:
    def __init__(self, name):
        self.name = name
        self.books = []
    def __repr__(self):
        return f'Publisher {self.name}'
class Author:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
        self.books = []
    def __repr__(self):
        return f'Author {self.firstname} {self.lastname}'