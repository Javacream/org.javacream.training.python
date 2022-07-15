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
        isbn = self.books_service.create("Demo", 200, 19.99)
        self.assertIsNotNone(isbn)
        book = self.books_service.find_by_isbn(isbn)
        self.assertIsNotNone(book)
        self.books_service.delete_by_isbn(isbn)
