class Book:
    def __init__(self, isbn, title, price):
        self.isbn = isbn
        self.title = title
        self.price = price

class  BooksService:
    def __init__(self):
        self.books = dict() # key= Isbn-Nummer, Value ist das komplette Book-Objekt
        self.actual_isbn = 0

    def create(self, title, price=0.0):
        self.actual_isbn += 1
        isbn = f'ISBN-{self.actual_isbn}'
        new_book = Book(isbn, title, price)
        self.books[isbn] = new_book
        return isbn

    def find_by_isbn(self, isbn):
        return self.books.get(isbn)

