from publishing.booksservice import BooksService
from publishing.isbngenerator import IsbnGenerator
from publishing.storeservice import StoreService


class Object(object):
    pass
def context():
    context = Object()
    context.bookservice = BooksService()
    context.storeservice = StoreService()
    context.isbngenerator = IsbnGenerator("Isbn:", "-de")
    context.bookservice.isbngenerator = context.isbngenerator
    context.bookservice.storeservice = context.storeservice
    return context
    