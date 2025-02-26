import socket
import pickle
from bmi import calculate_bmi 
from multiprocessing import Process
def handle_client_request(client_socket):
    with client_socket:    
        data = pickle.loads(client_socket.recv(1024))
        bmi = calculate_bmi(data[0], data[1])
        client_socket.sendall(str(bmi).encode())

def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8001
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((IP_ADDRESS, PORT))
        server_socket.listen(1)
        while True:
            client_socket, address_info = server_socket.accept()
            Process(target=handle_client_request, args=(client_socket, )).start()
if __name__ == '__main__':
    main()