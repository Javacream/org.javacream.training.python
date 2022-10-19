from books.booksservice import BooksService
from books.isbngenerator import IsbnGenerator
from books.storeservice import StoreService

isbngenerator = IsbnGenerator()
store_service = StoreService()
books_service = BooksService(store_service, isbngenerator)

