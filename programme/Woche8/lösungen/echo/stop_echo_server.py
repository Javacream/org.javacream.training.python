import socket
def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8001
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((IP_ADDRESS, PORT))

if __name__ == '__main__':
    main()