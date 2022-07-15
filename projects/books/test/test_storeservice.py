import sys
sys.path.append('../src')

from unittest2.case import TestCase
from javacream.storeservice import StoreService
class BooksServiceTest(TestCase):


    def setUp(self):
        self.store_service = StoreService()
    
    def test_works(self):
        pass
        

