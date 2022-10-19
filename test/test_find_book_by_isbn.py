import sys

sys.path.append('../src')

from unittest.case import TestCase

from books.booksservice import Book, BooksService
from books.isbngenerator import IsbnGenerator
from books.storeservice import StoreService


class FindBookByIsbnTest(TestCase):

    def setUp(self):
        self.service = BooksService(StoreService(), IsbnGenerator())
        self.isbn = self.service.create("Python", 19.99) 

    def test_find_by_isbn_works(self):
        book = self.service.find_by_isbn(self.isbn)
        self.assertEqual("Python", book.title)
    
