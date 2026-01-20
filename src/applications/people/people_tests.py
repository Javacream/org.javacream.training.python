from people_service import Person
import unittest
class PeopleTests(unittest.TestCase):
    def test_person_say_hello(self):
        lastname = 'Sawitzki'
        firstname = 'Rainer'

        expected_hello = 'Hello, my name is Rainer Sawitzki'

        p = Person(lastname, firstname)

        hello = p.say_hello()
        self.assertEqual(expected_hello, hello)

    def test_person_lastname(self):
        lastname = 'Sawitzki'
        firstname = 'Rainer'

        expected_lastname = 'Sawitzki'

        p = Person(lastname, firstname)

        self.assertEqual(expected_lastname, p.lastname)

class StudentTests(unittest.TestCase):
    def test_study(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()