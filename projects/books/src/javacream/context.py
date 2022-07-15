from turtle import st
from javacream.booksservice import BooksService
from javacream.isbngenerator import IsbnGenerator
from javacream.storeservice import StoreService


class Object:
    pass

def create_context():
    context = Object()
    store_service = StoreService()
    isbngenerator = IsbnGenerator("ISBN:", "-dk")
    books_service = BooksService(store_service, isbngenerator);
    context.store_service = store_service
    context.isbngenerator = isbngenerator
    context.books_service = books_service
    return context

context = create_context()