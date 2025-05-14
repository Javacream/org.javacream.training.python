import socket as socket_lib
def main():
    IP_ADDRESS = 'localhost' 
    PORT = 8000
    ENDPOINT = (IP_ADDRESS, PORT)
    with socket_lib.socket(socket_lib.AF_INET, socket_lib.SOCK_STREAM) as server_socket:
        server_socket.bind(ENDPOINT)
        server_socket.listen(1)
        print(server_socket)
        while True:
            client_socket, address_info = server_socket.accept() 
            with client_socket:
                print(f'Nach accept: Clientsocket = {client_socket}, Addressinfo={address_info}')
                client_message = client_socket.recv(1024).decode('utf-8')
                print(f'Received message from client: {client_message}')
                client_socket.sendall('OK'.encode('utf-8'))
if __name__ == '__main__': 
    main()