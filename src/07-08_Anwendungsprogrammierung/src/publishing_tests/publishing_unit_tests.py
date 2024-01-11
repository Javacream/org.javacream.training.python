import unittest

from publishing.booksservice import BooksService, BookException
from publishing.utilities import IllegalParameterException
from unittest.mock import MagicMock


class BooksServiceTest(unittest.TestCase):


    def setUp(self):
        self.booksservice = BooksService()
        isbngenerator = MagicMock();
        isbngenerator.next_isbn.return_value="ISBN:12-345-678-910-dk"
        storeservice = MagicMock()
        storeservice.get_stock.return_value=10
        self.booksservice.isbngenerator = isbngenerator
        self.booksservice.storeservice = storeservice


    def _testNewWithTitle(self):
        isbn = self.booksservice.new("TEST")
        #self.assertTrue(isbn, "ISBN must be generated")
        self.booksservice.isbngenerator.next_isbn.assert_called_once_with();
        self.assertEquals("ISBN:12-345-678-910-dk", isbn)
        

    def _testNewWithTitleAndPrice(self):
        self.booksservice.new("TEST", 19.99)
    def _testNewWithTitleAndPriceAndPages(self):
        self.booksservice.new("TEST", 19.99, 200)
    def _testNewWithNoneTitle(self):
        self.assertRaises(IllegalParameterException, self.booksservice.new, None)  
    def _testNewWithEmptyTitle(self):
        self.assertRaises(IllegalParameterException, self.booksservice.new, "   ")  
    def _testNewWithZeroPages(self):
        self.assertRaises(IllegalParameterException, self.booksservice.new, "TITLE", 0)  
    def _testNewWithNegativePages(self):
        self.assertRaises(IllegalParameterException, self.booksservice.new, "TITLE", -1)  
    def _testNewWithNegativePrice(self):
        self.assertRaises(IllegalParameterException, self.booksservice.new, "TITLE", 10, -.99)  
    
    
    def testFindBookByIsbn(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        book = self.booksservice.find_book_by_isbn(isbn)
        self.assertEqual(title, book.title)
        self.assertEqual(pages, book.pages)
        self.assertAlmostEqual(price, book.price, "Price must be %f" %(price), 1e-9)
        #mock
        self.assertTrue(book.available)
        self.booksservice.storeservice.get_stock.assert_called_once_with("books", "ISBN:12-345-678-910-dk")

    def _testDeleteBookByIsbn(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        self.booksservice.delete_book_by_isbn(isbn)

    def _testDeletedBookMustNotBeFound(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        self.booksservice.delete_book_by_isbn(isbn)
        self.assertRaises(BookException, self.booksservice.find_book_by_isbn, isbn)

    def _testUnknownBookCannotBeDeleted(self):
        self.assertRaises(BookException, self.booksservice.find_book_by_isbn, "__UNKNOWN__")

    def _testUnknownBookCannotBeFound(self):
        self.assertRaises(BookException, self.booksservice.find_book_by_isbn, "__UNKNOWN__")

    def _testUpdateBook(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        self.booksservice.update(isbn, pages=222, price=29.99)
        
    def _testUpdateBookWithPriceAndPagesChangesValues(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        changedPages = 222
        changedPrice = 29.99
        self.booksservice.update(isbn, pages=changedPages, price=changedPrice)
        book = self.booksservice.find_book_by_isbn(isbn)
        self.assertEqual(changedPages, book.pages)
        self.assertAlmostEqual(changedPrice, book.price, "Price must be %f" %(price), 1e-9)
        
    def _testUpdateBookWithPriceChangesPrice(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        changedPrice = 29.99
        self.booksservice.update(isbn, price=changedPrice)
        book = self.booksservice.find_book_by_isbn(isbn)
        self.assertEqual(pages, book.pages)
        self.assertAlmostEqual(changedPrice, book.price, "Price must be %f" %(price), 1e-9)        
        
    def _testUpdateBookWithPagesChangesPages(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        changedPages = 222
        self.booksservice.update(isbn, pages=changedPages)
        book = self.booksservice.find_book_by_isbn(isbn)
        self.assertEqual(changedPages, book.pages)
        self.assertAlmostEqual(price, book.price, "Price must be %f" %(price), 1e-9)
        
    def _testUpdateBookWithIllegalPriceNotPossible(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        changedPrice = -29.99
        self.assertRaises(BookException, self.booksservice.update, isbn, price=changedPrice)

    def _testUpdateBookWithUnknownIsbnNotPossible(self):
        self.assertRaises(BookException, self.booksservice.update, "__UNKNOWN", price=19.99, pages=200)


