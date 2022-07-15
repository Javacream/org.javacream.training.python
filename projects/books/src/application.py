
from javacream.storeservice import StoreService
from javacream.isbngenerator import IsbnGenerator
from javacream.booksservice import Book


if __name__ == '__main__':
    store_service = StoreService()
    print (store_service.get_stock("this", "that"))
    isbn_generator = IsbnGenerator()
    print (isbn_generator.next_isbn())
    book = Book(isbn_generator.next_isbn(), "Python", 200, 29.99)
    print(book)    
