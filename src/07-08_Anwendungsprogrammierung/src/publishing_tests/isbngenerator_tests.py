'''
Created on 04.11.2013

@author: rus
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        
        self.assertTrue(True)

    def test2(self):
        self.assertTrue(True)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()