from socketserver import TCPServer, BaseRequestHandler
import pickle
from bmi import calculate_bmi 
class BmiRequestHandler(BaseRequestHandler):
    def handle(self):
        data = pickle.loads(self.request.recv(1024))
        bmi = calculate_bmi(data[0], data[1])
        self.request.sendall(str(bmi).encode())

def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8001
    server = TCPServer((IP_ADDRESS, PORT), BmiRequestHandler)
    server.serve_forever()
if __name__ == '__main__':
    main()