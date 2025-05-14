import socket
def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((IP_ADDRESS, PORT))
        message = input("Bitte eine Nachricht eingeben: ")
        client_socket.sendall(message.encode('utf-8'))
        server_response = client_socket.recv(1024).decode()
        print(f'Response={server_response}')

if __name__ == '__main__':
    main()