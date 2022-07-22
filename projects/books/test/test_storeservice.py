import sys
sys.path.append('../src')

from unittest2.case import TestCase
from javacream.context import context
class BooksServiceTest(TestCase):

    def setUp(self):
        self.store_service = context.store_service
    
    def test_set_store_works(self):
        rnd = hash(object())
        print(rnd)
        self.store_service.set_stock("books", "Isbn" + str(rnd), 42)
        self.store_service.set_stock("dvd", "egal" + str(rnd), 4711)
    def xtest_set_store_service_creates_readable_entry(self):
        rnd = hash(object())
        print(rnd)
        category = "books"
        item = "Isbn1" + str(rnd)
        stock = 42
        self.store_service.set_stock(category, item, stock)
        result_stock = self.store_service.get_stock(category, item)
        self.assertEquals(stock, result_stock)
    def xtest_set_store_creates_categories(self):
        print(rnd)
        rnd = hash(object())
        self.store_service.set_stock("books", "Isbn" + str(rnd), 42)
        self.store_service.set_stock("dvd", "egal" + str(rnd), 4711)
        self.assertEquals(2, len(self.store_service.get_categories()))

    def xtest_set_store_creates_items_in_category(self):
        rnd = hash(object())
        print(rnd)
        self.store_service.set_stock("books", "Isbn1" + str(rnd), 42)
        self.store_service.set_stock("books", "Isbn2" + str(rnd), 42)
        self.assertEquals(2, len(self.store_service.get_items_for("books")))

    def xtest_unknown_category_has_empty_items(self):
        self.assertEquals(0, len(self.store_service.get_items_for("UNKNOWN")))

        
    

