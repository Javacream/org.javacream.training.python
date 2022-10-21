from books.booksservice import BooksService
from books.config import Configuration
from books.isbngenerator import IsbnGenerator
from books.storeservice import StoreService

configuration = Configuration()
isbngenerator = IsbnGenerator(configuration.get_isbngenerator_configuration('prefix'), configuration.get_isbngenerator_configuration('suffix'))
store_service = StoreService()
books_service = BooksService(store_service, isbngenerator)

