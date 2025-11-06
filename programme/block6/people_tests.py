import unittest
from people import Person, Address

class PeopleTests(unittest.TestCase):
    def test_demo(self):
        data = 'Hugo'
        expeceted_result = 'H'
        result = data[0]
        self.assertEqual(expeceted_result, result)

    def test_say_hello(self):
        p = Person('A', 'B', 188, 76.6, Address('some', 'where'))
        expeceted_result = 'Hello, my name is B A'
        result = p.say_hello()
        self.assertEqual(expeceted_result, result)

unittest.main()