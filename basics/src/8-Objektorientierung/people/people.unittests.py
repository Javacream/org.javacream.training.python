import unittest
from unittest.case import TestCase
from people import PeopleService 
class SimpleTest(TestCase):
    def testSimpleAssertion(self):
        number = 42
        self.assertEquals(42, number)

class PeopleServiceTest(TestCase):
    def testCreatePersonOk(self):
        ps = PeopleService()
        id = ps.create_person(self.lastname, self.firstname)
        self.assertIsNotNone(id)
    def setUp(self):
        self.lastname = "Mustermann"
        self.firstname = "Hans"
    def tearDown(self):
        print("***************")
    def testCreatedCanBeFound(self):
        ps = PeopleService()
        id = ps.create_person(self.lastname, self.firstname)
        person = ps.find_person_by_id(id)
        self.assertIsNotNone(person)
        self.assertEquals(self.lastname, person.lastname)
        self.assertEquals(self.firstname, person.firstname)




if __name__ == '__main__':
    unittest.main()

