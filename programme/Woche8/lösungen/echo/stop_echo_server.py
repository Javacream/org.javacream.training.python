import socket
def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((IP_ADDRESS, PORT))
        message = "secret_stop_code"
        client_socket.sendall(message.encode('utf-8'))

if __name__ == '__main__':
    main()