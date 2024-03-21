import unittest
import people

class PeopleTests(unittest.TestCase):
    def test_all(self):
        person =   {
            "id": 666,
            "lastname": "Testlastname",
            "firstname": "Testfirstname",
            "gender": "d",
            "height": 111
        }
        
        self.assertEqual("OK", people.create_person(person))
        search_result = people.find_by_id(person["id"])
        self.assertEqual("Testlastname", search_result["lastname"])
        self.assertTrue(isinstance(people.find_all(), list))
        person["lastname"] = "CHANGED"
        self.assertEqual("OK", people.update_person(person))
        search_result = people.find_by_id(person["id"])
        self.assertEqual("CHANGED", search_result["lastname"])
        self.assertEqual(200, people.delete_by_id(666))



unittest.main()