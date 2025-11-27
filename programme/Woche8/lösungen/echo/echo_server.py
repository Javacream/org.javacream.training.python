from socketserver import TCPServer, BaseRequestHandler
import configuration
import pickle
class EchoRequestHandler(BaseRequestHandler):
    def handle(self):
        messages_from_client = pickle.loads(self.request.recv(1024))
        result = [f'{message.lower()}\n' for message in messages_from_client]
        self.request.sendall(pickle.dumps(result))
                  
def main():
    endpoint = configuration.get_endpoint()
    echo_server = TCPServer(endpoint, EchoRequestHandler)
    echo_server.serve_forever()
if __name__ == '__main__':
    main()