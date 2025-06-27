import unittest
from rest_people_service import PeopleService

class PeopleServiceTests(unittest.TestCase):

    def test_read_people(self):
        endpoint = 'http://javacream.eu:8080/people' 
        expected_size = 15
        people_service = PeopleService(endpoint)
        result = people_service.read_people()
        self.assertEqual(expected_size, len(result))
    def test_read_people_from_invalid_endpoint(self):
        people_service = PeopleService('http://javacream.eu:8080/users')
        result = people_service.read_people()
        self.assertIsNone(result)

if __name__=='__main__':
    unittest.main()