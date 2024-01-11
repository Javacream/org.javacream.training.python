import socket 
import multiprocessing as mp
import os
class EchoServer:
    def __init__(self, ip_address, port):
        self.IP_ADDRESS = ip_address
        self.PORT = port
    def start_up(self):    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.bind((self.IP_ADDRESS, self.PORT))
            server_sock.listen(1)
            while True:
                client_sock, address_info = server_sock.accept()
                
                print(address_info)
                mp.Process(target=self.handle_client, args=(client_sock,)).start()

    def handle_client(self, client_sock):
        with client_sock:
            message = client_sock.recv(1024).decode()
            result = f'received {message} from {client_sock.getpeername()} using server process {os.getpid()}'
            print(result)
            client_sock.sendall(result.encode())

HOST, PORT = "127.0.0.1", 50505

def main():
    server = EchoServer(HOST, PORT)
    server.start_up()

if __name__ == '__main__': main()