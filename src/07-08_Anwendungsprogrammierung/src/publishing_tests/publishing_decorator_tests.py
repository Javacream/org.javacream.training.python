import unittest
from unittest.case import TestCase

from publishing.booksservice import BookException, BooksService
from publishing.isbngenerator import IsbnGenerator
from publishing.storeservice import StoreService
from publishing.utilities import IllegalParameterException
import testutilities


#from publishing_tests.testutilities import decorate
class BooksServiceTest(unittest.TestCase):


    def setUp(self):
        self.booksservice = BooksService()
        self.isbngenerator = IsbnGenerator()
        self.storeservice = StoreService()
        self.isbngenerator.prefix="TEST-ISBN:"
        self.isbngenerator.suffix="-de"
        self.booksservice.isbngenerator=self.isbngenerator
        self.booksservice.storeservice=self.storeservice
        testutilities.decorate(self.isbngenerator, testutilities.trace)
        testutilities.decorate(self.booksservice, testutilities.trace)
        
    def testNewWithTitle(self):
        isbn = self.booksservice.new("TEST")
        self.assertTrue(isbn, "ISBN must be generated")

    def testNewWithTitleAndPrice(self):
        self.booksservice.new("TEST", 19.99)
    def testNewWithTitleAndPriceAndPages(self):
        self.booksservice.new("TEST", 19.99, 200)
    def testNewWithNoneTitle(self):
        self.assertRaises(IllegalParameterException, self.booksservice.new, None)  
    def testNewWithEmptyTitle(self):
        self.assertRaises(IllegalParameterException, self.booksservice.new, "   ")  
    def testNewWithZeroPages(self):
        self.assertRaises(IllegalParameterException, self.booksservice.new, "TITLE", 0)  
    def testNewWithNegativePages(self):
        self.assertRaises(IllegalParameterException, self.booksservice.new, "TITLE", -1)  
    def testNewWithNegativePrice(self):
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

    def testDeleteBookByIsbn(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        self.booksservice.delete_book_by_isbn(isbn)

    def testDeletedBookMustNotBeFound(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        self.booksservice.delete_book_by_isbn(isbn)
        self.assertRaises(BookException, self.booksservice.find_book_by_isbn, isbn)

    def testUnknownBookCannotBeDeleted(self):
        self.assertRaises(BookException, self.booksservice.find_book_by_isbn, "__UNKNOWN__")

    def testUnknownBookCannotBeFound(self):
        self.assertRaises(BookException, self.booksservice.find_book_by_isbn, "__UNKNOWN__")

    def testUpdateBook(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        self.booksservice.update(isbn, pages=222, price=29.99)
        
    def testUpdateBookWithPriceAndPagesChangesValues(self):
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
        
    def testUpdateBookWithPriceChangesPrice(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        changedPrice = 29.99
        self.booksservice.update(isbn, price=changedPrice)
        book = self.booksservice.find_book_by_isbn(isbn)
        self.assertEqual(pages, book.pages)
        self.assertAlmostEqual(changedPrice, book.price, "Price must be %f" %(price), 1e-9)        
        
    def testUpdateBookWithPagesChangesPages(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        changedPages = 222
        self.booksservice.update(isbn, pages=changedPages)
        book = self.booksservice.find_book_by_isbn(isbn)
        self.assertEqual(changedPages, book.pages)
        self.assertAlmostEqual(price, book.price, "Price must be %f" %(price), 1e-9)
        
    def testUpdateBookWithIllegalPriceNotPossible(self):
        title = "TEST"
        pages = 200
        price = 19.99
        isbn = self.booksservice.new(title, pages, price)
        changedPrice = -29.99
        self.assertRaises(BookException, self.booksservice.update, isbn, price=changedPrice)

    def testUpdateBookWithUnknownIsbnNotPossible(self):
        self.assertRaises(BookException, self.booksservice.update, "__UNKNOWN", price=19.99, pages=200)


class IsbnGeneratorTest(TestCase):
    def setUp(self):
        self.isbngenerator = IsbnGenerator()
        self.PREFIX = "TEST:"
        self.SUFFIX = "-dk"
        self.isbngenerator.prefix=self.PREFIX
        self.isbngenerator.suffix=self.SUFFIX
        
        
    def testIsbnGeneration(self):
        isbn = self.isbngenerator.next_isbn()
        self.assertTrue(isbn, "ISBN must be generated")
    def testIsbnGenerationStartsWithPrefix(self):
        isbn = self.isbngenerator.next_isbn()
        self.assertTrue(isbn.startswith(self.PREFIX), "ISBN must start with %s" %(self.PREFIX))
    def testIsbnGenerationEndsWithSuffix(self):
        isbn = self.isbngenerator.next_isbn()
        self.assertTrue(isbn.endswith(self.SUFFIX), "ISBN must end  with %s" %(self.SUFFIX))
            
            
class StoreServiceTest(unittest.TestCase):
    def setUp(self):
        self.storeservice = StoreService()
    
    def testRetrieveStock(self):
        self.storeservice.get_stock("category", "item")            
    def testRetrieveStockWithUnknownCategoryRetrievesZero(self):
        stock = self.storeservice.get_stock("__UNKNOWN__", "item")
        self.assertEqual(0, stock);
    def testRetrieveStockWithNoneCategoryFails(self):
        self.assertRaises(IllegalParameterException, self.storeservice.get_stock, None, "item")
    def testRetrieveStockWithNoneItemFails(self):
        self.assertRaises(IllegalParameterException, self.storeservice.get_stock, "category", None)
    def testRetrieveStockWithUnknownItemRetrievesZero(self):
        stock = self.storeservice.get_stock("category", "__UNKNOWN__")
        self.assertEqual(0, stock);
                            