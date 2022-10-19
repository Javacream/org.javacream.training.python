import unittest
import sys
sys.path.append('../src')
from unittest.case import TestCase

class ScratchTests(TestCase):
    def setUp(self):
        print("SETUP")
    def tearDown(self):
        print("DOWN")
    def test_simple(self):
        self.assertTrue(True)
    def test_simple(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()