import os 
dir_path = os.path.dirname(os.path.realpath(__file__))


import sys
sys.path.append(dir_path + '/..')

#from javacream.storeservice import StoreService
#from javacream.isbngenerator import IsbnGenerator
from javacream.booksservice import Book
from javacream.context import context

if __name__ == '__main__':
    store_service = context.store_service
    print (store_service.get_stock("this", "that"))
    isbn_generator = context.isbngenerator
    print (isbn_generator.next_isbn())
    book = Book(isbn_generator.next_isbn(), "Python", 200, 29.99)
    print(book)    

    store_service.set_stock("books", "Isbn1", 42)
    store_service.set_stock("books", "Isbn2", 41)
    store_service.set_stock("dvd", "egal", 4711)
    print (store_service.get_stock("books", "Isbn1"))
    print(store_service.get_categories())
    print(store_service.get_items_for("books"))
    print(store_service.get_items_for("unknown"))

