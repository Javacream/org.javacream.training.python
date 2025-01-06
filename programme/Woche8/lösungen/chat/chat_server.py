import socket 
import multiprocessing as mp
class ChatServer:
    def __init__(self, ip_address, port):
        self.IP_ADDRESS = ip_address
        self.PORT = port
        self.messages = {}
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
            user = client_sock.recv(10+24).decode()
            self.messages[user] = []
            client_sock.sendall(f'Guten Tag, {user}'.encode())
            try:
                while True:
                    message = client_sock.recv(1024).decode()
                    self.messages[user].append(message)
                    client_sock.sendall(f'{user} schickte Nachricht {message}'.encode())
                    print(self.messages)
            except:
                print('connection closed')