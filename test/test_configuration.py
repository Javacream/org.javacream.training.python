import sys

sys.path.append('../src')

from unittest.case import TestCase

from books.config import Configuration


class TestConfiguration(TestCase):

    def setUp(self):
        self.configuration = Configuration()

    def test_isbngenerator_config_has_prefix(self):
        self.assertEqual("Isbn-", self.configuration.get_isbngenerator_configuration()['prefix'])
            
    def test_isbngenerator_config_has_suffix(self):
        self.assertEqual("-dk", self.configuration.get_isbngenerator_configuration()['suffix'])
