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

    def test_representation(self):
        p = Person('B', 'A', 100, 200)
        expected_representation = 'Person(lastname=B, firstname=A, height=100, weight=200)'
        #print(p)
        #calculated_representation = p.__repr__()
        calculated_representation = repr(p)
        self.assertTrue(calculated_representation.startswith(expected_representation), f'{calculated_representation} does not start with {expected_representation}')
    
    def test_object(self):
        o = object()
        self.assertIsNotNone(o)
    
unittest.main()