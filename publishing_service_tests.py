import unittest
import publishing_service
from publishing import Publisher
class PublishingServiceTest(unittest.TestCase):
    def testPublishingServiceCreatesAPublisher(self):
        name = 'Springer'
        p = publishing_service.create_publisher(name)
        self.assertEqual(name, p.name)
    def test_find_all_publishers_sorted_by_name(self):
        publisher_dict = {'P': Publisher("P"), 'A': Publisher("A"), 'Z': Publisher("Z")}
        publishing_service.publishers = publisher_dict
        sorted_publisher = publishing_service.find_all_publishers_sorted_by_name()
        self.assertEqual(sorted_publisher[0].name, 'A')
if __name__ == '__main__':
    unittest.main()