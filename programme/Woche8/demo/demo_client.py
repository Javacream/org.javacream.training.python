import socket as socket_lib
def main():
    IP_ADDRESS = 'localhost' # Das ist in der Realität eine Host-Adresse
    PORT = 8000
    ENDPOINT = (IP_ADDRESS, PORT)
    with socket_lib.socket(socket_lib.AF_INET, socket_lib.SOCK_STREAM) as client_socket:
        print(f'Client Socket vor connect: {client_socket}')
        client_socket.connect(ENDPOINT)
        print(f'Client Socket nach connect: {client_socket}')
        client_socket.sendall('Hello'.encode('utf-8'))
        server_message = client_socket.recv(1024).decode('utf-8')
        print(f'Received response message from server: {server_message}')

if __name__ == '__main__': 
    main()