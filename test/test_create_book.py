import sys

sys.path.append('../src')

from unittest.case import TestCase

from books.booksservice import BookException
# from books.isbngenerator import IsbnGenerator
# from books.storeservice import StoreService
from books.application_context_remote import books_service

class CreateBookTest(TestCase):

    def setUp(self):
        self.service = books_service
    def test_create_book_works(self):
        isbn = self.service.create("Python", 19.99) 
        self.assertIsNotNone(isbn)

    def test_create_book_works(self):
        self.assertRaises(BookException, lambda: self.service.create(None, 19.99)) 

    # def test_create_book_works2(self):
    #     self.assertRaises(BookException, self.throwBookException) 

    # def throwBookException(self):
    #     self.service.create(None, 6.66)