from javacream.booksservice import BooksService
from javacream.isbngenerator import IsbnGenerator
from javacream.storeservice import StoreService


class Object:
    pass

def context():
    context = Object()
    context.bookservice = BooksService()
    context.storeservice = StoreService()
    context.isbngenerator = IsbnGenerator("Isbn:", "-de")
    context.bookservice.isbngenerator = context.isbngenerator
    context.bookservice.storeservice = context.storeservice
    return context
