class Book:
    def __init__(self, isbn, title, price, pages, available):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.pages = pages
        self.available = available
    def __repr__(self):
        return f'Book: isbn={self.isbn}, title={self.title}, price={self.price}, pages={self.pages}, available={self.available}'
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        else:
            return False
    def __hash__(self):
        return hash(self.isbn)    