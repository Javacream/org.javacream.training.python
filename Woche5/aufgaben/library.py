class Book:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title

class Library:
    def __init__(self):
        self.books = dict()

    def add(self, book):
        self.books.update(book.isbn, book)
    def lend(self, isbn):
        return self.books.get(isbn)    
    def all_books(self):
        return self.books.values()