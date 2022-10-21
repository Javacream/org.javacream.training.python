import sys

sys.path.append('../src')


from unittest.case import TestCase

from books.isbngenerator import IsbnGenerator


class IsbngeneratorTest(TestCase):


    def setUp(self):
        self.isbngenerator = IsbnGenerator()
    
    def test_isbngenerator_generated_isbn(self):
        isbn = self.isbngenerator.next_isbn()
        self.assertIsNotNone(isbn)
    def test_isbngenerator_generates_unique_isbns(self):
        isbn1 = self.isbngenerator.next_isbn()
        isbn2 = self.isbngenerator.next_isbn()
        self.assertNotEqual(isbn1, isbn2)