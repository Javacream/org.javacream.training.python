import unittest
from remote_service import RemoteService

class RemoteServiceTests(unittest.TestCase):
    def test_upload_and_execute_simple_py(self):
        config = {
            'port': 22,
            'username': 'teilnehmer',
            'password': 'javacream123!'
        }
        remote_service = RemoteService('javacream.eu', config)
        result = remote_service.upload_and_execute('programme/Präsenztag10/todo_slide_157/simple.py')
        self.assertEqual('', result[1])
        self.assertEqual('Hello\n', result[0])

if __name__ == '__main__':
    unittest.main()
