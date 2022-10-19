import sys

sys.path.append('../src')

from unittest.case import TestCase

from books.booksservice import Book, BooksService
from books.isbngenerator import IsbnGenerator
from books.storeservice import StoreService


class UpdateBookTest(TestCase):

    def setUp(self):
        self.service = BooksService(StoreService(), IsbnGenerator())
        self.isbn = self.service.create("Python", 19.99) 

    def test_update_books_works(self):
        book = Book(self.isbn, "Changed", 9.99)
        self.service.update(book)
        searchedBook = self.service.find_by_isbn(self.isbn)
        self.assertEqual(9.99, book.price);
        self.assertEqual("Changed", book.title);
