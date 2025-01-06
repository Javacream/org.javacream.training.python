import unittest
import socket
class ChatServerTests(unittest.TestCase):
    def setUp(self):
        IP_ADDRESS = '127.0.0.1' # 'localhost'
        PORT = 12346
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((IP_ADDRESS, PORT))

    def tearDown(self):
        self.client_socket.close()
    def test_user_is_accepted(self):
        self.client_socket.sendall('Test'.encode('utf-8'))
        greeting = self.client_socket.recv(1024).decode()
        self.assertEqual('Guten Tag, Test', greeting)
    def test_message_is_accepted(self):
        self.client_socket.sendall('Test'.encode('utf-8'))
        greeting = self.client_socket.recv(1024).decode()
        self.client_socket.sendall('Hello'.encode())
        response = self.client_socket.recv(1024).decode()
        self.assertEqual('Test schickte Nachricht Hello', response) # Annahme: '{name} schickte Nachricht {message}

if __name__ == '__main__':
    unittest.main()

