from books.booksservice import BooksService
from books.isbngenerator import IsbnGenerator
from books.storeservice import StoreService

isbngenerator = IsbnGenerator()
storeService = StoreService()
booksService = BooksService(storeService, isbngenerator)

