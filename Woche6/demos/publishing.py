class Book:
    def __init__(self, isbn, title, pages, price):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.pages = pages
    def __repr__(self):
        return f"Book: isbn={self.isbn}, title={self.title}, pages={self.pages}, price={self.price}, "
    

class BooksController:
    def __init__(self, isbn_generator):
        self.isbn_generator = isbn_generator
    def create(self, title, pages=0, price=9.99):
        isbn = self.isbn_generator.next_isbn()
        new_book = Book(isbn, title, pages, price)
        return new_book

class IsbnGenerator:
    def __init__(self):
        self.isbn_counter = 0
    def next_isbn(self):    
        self.isbn_counter += 1
        isbn = f"ISBN-{self.isbn_counter}-de"
        return isbn

def test():
    isbn_generator = IsbnGenerator()
    books_controller = BooksController(isbn_generator)
    book1 = books_controller.create("title1", 200, 19.99)
    print(book1)
    print(book1.isbn)
test()