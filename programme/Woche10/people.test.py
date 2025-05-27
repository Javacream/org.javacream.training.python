import unittest
from people import PeopleService

class PeopleServiceGetTest(unittest.TestCase):
    def test_get_people(self):
        ps = PeopleService('http://javacream.eu:8080/people')
        people_list = ps.get_people()
        self.assertEqual(10, len(people_list))

if __name__ == '__main__':
    unittest.main()