a_list = list()

print(type(a_list))

class Book:
    def __init__(self, isbn, title, price, available):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.available = available

a_book = Book('ISBN1', 'Python in Action', 19.99, True) # a_book ist eine Instanz der Klasse Book, die durch einen Konstruktor-Aufruf erzeugt wird
print(type(a_book))

#a_book.isbn = 'ISBN1'
#a_book.title = 'Python in Action'
#a_book.price = 19.99
#a_book.available = True

print('done')