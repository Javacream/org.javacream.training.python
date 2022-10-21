from books.booksservice import RestClientBooksService
from books.config import Configuration
from books.isbngenerator import IsbnGenerator
from books.storeservice import DatabaseStoreService

configuration = Configuration()
isbngenerator = IsbnGenerator(configuration.get_isbngenerator_configuration()['prefix'], configuration.get_isbngenerator_configuration()['suffix'])
store_service = DatabaseStoreService(configuration.get_database_configuration())
books_service = RestClientBooksService(configuration.get_configuration('endpoint')['url'], store_service)

