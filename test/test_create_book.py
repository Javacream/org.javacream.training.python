import sys

sys.path.append('../src')

from unittest.case import TestCase

from books.booksservice import BookException, BooksService
from books.isbngenerator import IsbnGenerator
from books.storeservice import StoreService


class CreateBookTest(TestCase):

    def setUp(self):
        self.service = BooksService(StoreService(), IsbnGenerator())
    def test_create_book_works(self):
        isbn = self.service.create("Python", 19.99) 
        self.assertIsNotNone(isbn)

    def test_create_book_works(self):
        self.assertRaises(BookException, lambda: self.service.create(None, 19.99)) 

    # def test_create_book_works2(self):
    #     self.assertRaises(BookException, self.throwBookException) 

    # def throwBookException(self):
    #     self.service.create(None, 6.66)