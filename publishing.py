class Book:
    def __init__(self, isbn, title, price, pages, publisher):
        self.isbn =isbn
        self.title = title
        self.price = price
        self.pages = pages
        self.authors = set()
        self.publisher = publisher

class Publisher:
    def __init__(self, name):
        self.name = name
        self.books = []

class Author:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
        self.books = []
