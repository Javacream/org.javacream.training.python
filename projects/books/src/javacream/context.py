import mysql.connector
from javacream.booksservice import RestClientBooksService, BooksService
from javacream.isbngenerator import IsbnGenerator
from javacream.storeservice import StoreService, DatabaseStoreService
from javacream.decorators import decorate, debug

import logging

file = logging.FileHandler('./books_prod.log')
console = logging.StreamHandler()#Standard: Streaming auf die Konsole
file.setLevel(logging.DEBUG)
console.setLevel(logging.INFO)
logging.basicConfig(level=logging.DEBUG, handlers=[file, console])


class Object:
    pass


def create_context():
    db_config = {
        "host": "h2908727.stratoserver.net",
        "port": 3406,
        "database": "javacream",
        "user": "user",
        "password": "user"
    }
    database = mysql.connector.connect(**db_config)

    context = Object()
    store_service = DatabaseStoreService(database)
    isbngenerator = IsbnGenerator("ISBN:", "-dk")
    #books_service = BooksService(store_service, isbngenerator) # local
    books_service = RestClientBooksService(store_service) # remote
    context.store_service =  decorate(store_service, debug)
    context.isbngenerator = decorate(isbngenerator, debug)
    context.books_service = decorate(books_service, debug)
    return context

context = create_context()