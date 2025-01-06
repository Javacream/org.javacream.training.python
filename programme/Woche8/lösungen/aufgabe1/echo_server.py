import socket 
def main():
    IP_ADDRESS = '127.0.0.1' # 'localhost' oder das Ergebnis von ipconfig (Windows) ip -A
    PORT = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((IP_ADDRESS, PORT))
        server_sock.listen(1)
        while True:
            client_sock, address_info = server_sock.accept()
            print(address_info)
            message_from_client = client_sock.recv(10+24)
            message_from_client = message_from_client.decode()
            print(f'Received: {message_from_client}')
            client_sock.sendall(f'From Server: {message_from_client}'.encode())


if __name__ == '__main__':
    main()