import logging

from books.booksservice import BooksService
from books.config import Configuration
from books.decorators import decorate, trace
from books.isbngenerator import IsbnGenerator
from books.storeservice import StoreService

file = logging.FileHandler('./books.log')
console = logging.StreamHandler() # Standard: Konsole
file.setLevel(logging.INFO)
console.setLevel(logging.INFO)

logging.basicConfig(level=logging.INFO, handlers=[console, file])
#logging.getLogger("books.decorators").setLevel(logging.DEBUG)
configuration = Configuration()
isbngenerator = IsbnGenerator(configuration.get_isbngenerator_configuration()['prefix'], configuration.get_isbngenerator_configuration()['suffix'])
store_service = StoreService()
books_service = BooksService(isbngenerator, store_service)
books_service = decorate(books_service, trace)

