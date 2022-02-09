import unittest
from unittest import IsolatedAsyncioTestCase
from books import BooksService

class BooksServiceTest(IsolatedAsyncioTestCase):

    async def testFindBookByIsbnISBN1FindsBook(self):
        booksService = BooksService()
        book = await booksService.find_by_isbn("ISBN1")
        self.assertIsNotNone(book)
        self.assertEqual('Java', book.title)

    async def testFindAllBooks(self):
        booksService = BooksService()
        books = await booksService.find_all()
        self.assertIsNotNone(books)
        print(len(books))

if __name__ == '__main__':
    unittest.main()
