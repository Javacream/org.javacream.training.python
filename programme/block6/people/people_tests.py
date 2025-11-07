import unittest
from people import Person
class PeopleTests(unittest.TestCase):
    def test_person(self):
        lastname = 'A'
        firstname = 'B'
        height = 100
        weight = 200

        expected_greeting = 'Hello, my name is B A'
        
        p = Person(lastname, firstname, height, weight)
        greeting = p.greet()

        self.assertEqual(expected_greeting, greeting)
unittest.main()