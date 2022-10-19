import sys

sys.path.append('../src')

from unittest.case import TestCase

from books.booksservice import Book, BooksService
from books.isbngenerator import IsbnGenerator
from books.storeservice import StoreService


class DeleteBookTest(TestCase):

    def setUp(self):
        self.service = BooksService(StoreService(), IsbnGenerator())
        self.isbn = self.service.create("Python", 19.99) 

    def test_delete_book_by_isbn(self):
        self.service.delete_by_isbn(self.isbn)


    
