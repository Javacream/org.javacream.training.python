import sys
sys.path.append('../src')

from unittest2.case import TestCase
#from javacream.isbngenerator import IsbnGenerator
from javacream.context import context
class BooksServiceTest(TestCase):


    def setUp(self):
        self.isbngenerator = context.isbngenerator
    
    def test_isbngenerator_generated_isbn(self):
        isbn = self.isbngenerator.next_isbn()
        self.assertIsNotNone(isbn)
    def test_isbngenerator_generates_unique_isbns(self):
        isbn1 = self.isbngenerator.next_isbn()
        isbn2 = self.isbngenerator.next_isbn()
        self.assertNotEquals(isbn1, isbn2)
