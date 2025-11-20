class Book:
    def __init__(self, isbn, title, price, available):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.available = available

def main():
    book1 = Book('ISBN-1', 'Title-1', 19.99, True)
    book2 = Book('ISBN-2', 'Title-2', 91.99, False)
    print('done')
main()