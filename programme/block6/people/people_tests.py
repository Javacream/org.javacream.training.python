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
        print(Person.get_people_count())


    def test_print_person(self):
        p = Person('A', 'B', 188, 76.6, Address('some', 'where'))
        expected_representation = 'Person(lastname=A, firstname=B, height=188, weight=76.6)'
        # representation = p.__repr__()
        representation = repr(p)
        self.assertEqual(expected_representation, representation)

    def test_people_equality(self):
        p1 = Person('A', 'B', 188, 76.6, Address('some', 'where'))
        p2 = Person('X', 'Y', 148, 96.6, Address('some', 'where'))
        p3 = p1
        p4 = Person('A', 'B', 188, 76.6, Address('some', 'where'))

        self.assertFalse(p1 == p2)
        self.assertTrue(p1 == p3)
        self.assertFalse(p1 == p4)


    def test_address_equality(self):
        a1 = Address('some', 'where')
        a2 = Address('any', 'place')
        a3 = a1
        a4 = Address('some', 'where')

        self.assertFalse(a1 == a2)
        self.assertTrue(a1 == a3)
        self.assertTrue(a1 == a4)

    def test_people_greatness(self):
        p1 = Person('A', 'B', 188, 76.6, Address('some', 'where'))
        p2 = Person('X', 'Y', 148, 96.6, Address('some', 'where'))
        self.assertTrue(p1 > p2)

    def test_people_add_weight(self):
        p1 = Person('A', 'B', 188, 76.6, Address('some', 'where'))
        print(p1.weight)
        p1 = p1 + 12.3
        print(p1.weight)

unittest.main()