'''
Created on 05.11.2013

@author: rus
'''
import pickle
from pprint import pprint
import unittest


class Test(unittest.TestCase):


    def testName(self):
        try:
            pickleFile = open("books.pkl", "rb")
            pprint (pickle.load(pickleFile))
        except IOError as e:
            print ("Error unpickling: " + str(e))
