import unittest
import publishing_service
class PublishingServiceTest(unittest.TestCase):
    def testPublishingServiceCreatesAPublisher(self):
        name = 'Springer'
        p = publishing_service.create_publisher(name)
        self.assertEqual(name, p.name)

if __name__ == '__main__':
    unittest.main()