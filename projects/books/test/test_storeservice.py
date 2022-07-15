import sys
sys.path.append('../src')

from unittest2.case import TestCase
from javacream.storeservice import StoreService
class BooksServiceTest(TestCase):


    def setUp(self):
        self.store_service = StoreService()
    
    def test_set_store_works(self):
        self.store_service.set_stock("books", "Isbn1", 42)
        self.store_service.set_stock("dvd", "egal", 4711)
    def test_set_store_service_creates_readable_entry(self):
        category = "books"
        item = "Isbn1"
        stock = 42
        self.store_service.set_stock(category, item, stock)
        result_stock = self.store_service.get_stock(category, item)
        self.assertEquals(stock, result_stock)
    def test_set_store_creates_categories(self):
        self.store_service.set_stock("books", "Isbn1", 42)
        self.store_service.set_stock("dvd", "egal", 4711)
        self.assertEquals(2, len(self.store_service.get_categories()))

    def test_set_store_creates_items_in_category(self):
        self.store_service.set_stock("books", "Isbn1", 42)
        self.store_service.set_stock("books", "Isbn2", 42)
        self.assertEquals(2, len(self.store_service.get_items_for("books")))

    def test_unknown_category_has_empty_items(self):
        self.assertEquals(0, len(self.store_service.get_items_for("books")))

        
    

