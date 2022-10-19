import unittest
import sys
sys.path.append('../src')
from unittest2.case import TestCase

class PeopleTests(TestCase):
    def test_simple(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()