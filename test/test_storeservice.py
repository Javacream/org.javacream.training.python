import sys

sys.path.append('../src')

from unittest.case import TestCase

from books.storeservice import StoreService


class StoreServiceTest(TestCase):

    def setUp(self):
        self.store_service = StoreService()
        self.store_service.set_stock('book', 'Isbn1', 42)
        self.store_service.set_stock('cd', 'Abbey Road', 5)

    

    def test_category_book_and_item_Isbn1_has_stock_42(self):
        self.assertEqual(42, self.store_service.get_stock('book', 'Isbn1'))

    def test_category_cd_and_item_AbbeyRoad_has_stock5(self):
        self.assertEqual(5, self.store_service.get_stock('cd', 'Abbey Road'))
    def test_unknown_category_has_stock0(self):
        self.assertEqual(0, self.store_service.get_stock('UNKNOWN', 'Abbey Road'))
    def test_unknown_item_has_stock0(self):
        self.assertEqual(0, self.store_service.get_stock('cd', 'UNKNOWN'))
        
    
