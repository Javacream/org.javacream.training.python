import logging

from books.booksservice import RestClientBooksService
from books.config import Configuration
from books.decorators import decorate, trace
from books.isbngenerator import IsbnGenerator
from books.storeservice import DatabaseStoreService

file = logging.FileHandler('./books.log')
console = logging.StreamHandler() # Standard: Konsole
file.setLevel(logging.DEBUG)
console.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, handlers=[console, file])

configuration = Configuration()
isbngenerator = IsbnGenerator(configuration.get_isbngenerator_configuration()['prefix'], configuration.get_isbngenerator_configuration()['suffix'])
store_service = DatabaseStoreService(configuration.get_database_configuration())
books_service = RestClientBooksService(configuration.get_configuration('endpoint')['url'], store_service)
books_service = decorate(books_service, trace)

