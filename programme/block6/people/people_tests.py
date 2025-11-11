import unittest
from people import Person, Address
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

    def test_person_equality(self):
        p1 = Person('B', 'A', 100, 200)
        p2 = Person('X', 'Y', 130, 60)
        p3 = p1
        p4 = Person('B', 'A', 100, 200)

        self.assertFalse(p1 == p2)
        self.assertTrue(p1 == p3)
        self.assertFalse(p1 == p4)

    def test_address_equality(self):
        a1 = Address('B', 'A')
        a2 = Address('X', 'Y')
        a3 = a1
        a4 = Address('B', 'A')

        self.assertFalse(a1 == a2)
        self.assertTrue(a1 == a3)
        self.assertTrue(a1 == a4)

    def test_person_adds_weight(self):
        p = Person('B', 'A', 100, 200)
        self.assertAlmostEqual(200, p.weight, 2)
        # ich möchte folgendes:
        p = p + 11.1
        self.assertAlmostEqual(211.1, p.weight, 2)

unittest.main()