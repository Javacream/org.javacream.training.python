import sys
sys.path.append('../src')

from unittest2.case import TestCase
#from javacream.isbngenerator import IsbnGenerator
from javacream.context import context
import testutils
class BooksServiceTest(TestCase):


    def setUp(self):
        self.books_service = testutils.decorate(context.books_service, testutils.trace)
    
    def test_sequence(self):
        isbn = self.books_service.create("Demo", 19.99)
        self.assertIsNotNone(isbn)
        book = self.books_service.find_by_isbn(isbn)
        self.assertIsNotNone(book)
        self.books_service.delete_by_isbn(isbn)
        books = self.books_service.find_all()
        self.assertIsNotNone(books)
        books_filtered_by_availability = [book for book in books if book.available]
        print(books_filtered_by_availability)
        min = 8
        max = 18
        books_filtered_by_price_range = [book for book in books if book.price > min and book.price < max]
        print(books_filtered_by_price_range)

