import socket
import pickle
from bmi import calculate_bmi 
def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8001
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((IP_ADDRESS, PORT))
        server_socket.listen(1)
        while True:
            client_socket, address_info = server_socket.accept()
            data = pickle.loads(client_socket.recv(1024))
            bmi = calculate_bmi(data[0], data[1])
            client_socket.sendall(str(bmi).encode())
if __name__ == '__main__':
    main()