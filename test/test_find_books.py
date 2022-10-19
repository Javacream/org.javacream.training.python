import sys

sys.path.append('../src')

from unittest.case import TestCase

from books.booksservice import BooksService
from books.isbngenerator import IsbnGenerator
from books.storeservice import StoreService


class FindAllBooksTest(TestCase):

    def setUp(self):
        self.service = BooksService(isbngenerator=IsbnGenerator(), store_service=StoreService())
        self.isbn = self.service.create("Python", 19.99) 
        self.isbn = self.service.create("Java", 9.99) 

    def test_find_all_books_has_2_elements(self):
        books = self.service.find_all()
        self.assertEqual(2, len(books))
