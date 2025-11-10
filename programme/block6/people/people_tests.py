import unittest
from people import Person, Address

class PeopleTests(unittest.TestCase):

    def test_say_hello(self):
        p = Person('A', 'B', 188, 76.6, Address('some', 'where'))
        expeceted_result = 'Hello, my name is B A'
        result = p.say_hello()
        self.assertEqual(expeceted_result, result)


    def test_print_person(self):
        p = Person('A', 'B', 188, 76.6, Address('some', 'where'))
        expected_representation_starts_with = '<people.Person object at '
        # representation = p.__repr__()
        representation = repr(p)
        self.assertTrue(representation.startswith(expected_representation_starts_with), f'{representation} does not start with {expected_representation_starts_with}')
unittest.main()