class Book:
    def __init__(self, isbn, title, price):
        self.isbn = isbn
        self.title = title
        self.price = price
    def __repr__(self):
        return f'Book: isbn={self.isbn}, title={self.title}, price={self.price}'
    def __eq__(self, other):
        return self.isbn == other.isbn
    def __hash__(self):
        return hash(self.isbn)