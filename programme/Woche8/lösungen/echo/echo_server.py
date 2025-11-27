import socket
import configuration
import pickle
class EchoServer:
    def __init__(self, endpoint):
        self.endpoint = endpoint
    def handle_client_request(self, client_socket):
            with client_socket:
                messages_from_client = pickle.loads(client_socket.recv(1024))
                result = [f'{message.lower()}\n' for message in messages_from_client]
                client_socket.sendall(pickle.dumps(result))
    def init(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(self.endpoint)
        server_socket.listen(1)
        self.server_socket = server_socket
    def listen(self):
        while True:
            client_socket, address_info = self.server_socket.accept()
            self.handle_client_request(client_socket)
                  
def main():
    endpoint = configuration.get_endpoint()
    echo_server = EchoServer(endpoint)
    try:
        echo_server.init()
        try:
            echo_server.listen()
        except Exception as e:
            print(f'exception listening to client request: {e}')    
        
    except Exception as e:
        print(f'cannot bind to {endpoint}: {e}')    
if __name__ == '__main__':
    main()