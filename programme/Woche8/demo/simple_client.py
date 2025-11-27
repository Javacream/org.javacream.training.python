import socket

def main():
    IP_ADDRESS = '127.0.0.1' #'localhost'
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print(client_socket)
        client_socket.connect((IP_ADDRESS, PORT))
        print(client_socket)
        client_socket.sendall('Hello'.encode('utf-8'))

main()