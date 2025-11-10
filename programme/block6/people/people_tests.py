import unittest
from people import Person, Address

class PeopleTests(unittest.TestCase):
    def test_object(self):
        o = object()
        self.assertIsNotNone(o)

    def test_say_hello(self):
        p = Person('A', 'B', 188, 76.6, Address('some', 'where'))
        expeceted_result = 'Hello, my name is B A'
        result = p.say_hello()
        self.assertEqual(expeceted_result, result)


    def test_print_person(self):
        p = Person('A', 'B', 188, 76.6, Address('some', 'where'))
        expected_representation = 'Person(lastname=A, firstname=B, height=188, weight=76.6)'
        # representation = p.__repr__()
        representation = repr(p)
        self.assertEqual(expected_representation, representation)
unittest.main()