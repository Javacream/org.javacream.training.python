import unittest
from database_people_service import PeopleService

class PeopleServiceTests(unittest.TestCase):

    def test_read_people(self):
        config = {
            'host': 'javacream.eu',
            'port': 3406,
            'database': 'javacream',
            'user': 'user',
            'password': 'user'

        }
        expected_size = 100
        people_service = PeopleService(config)
        result = people_service.read_people()
        self.assertEqual(expected_size, len(result))
    def xtest_read_people_from_invalid_endpoint(self):
        people_service = PeopleService('http://javacream.eu:8080/users')
        result = people_service.read_people()
        self.assertIsNone(result)

if __name__=='__main__':
    unittest.main()