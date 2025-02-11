class Book:
    def __init__(self, isbn, title, pages, price, available):
        self.isbn = isbn
        self.title = title
        self.pages = pages
        self.price = price
        set.available = available
    
    def info(self):
        return f'Book: isbn={self.isbn}, title={self.title}, price={self.price}, pages={self.pages}, available={self.available}'