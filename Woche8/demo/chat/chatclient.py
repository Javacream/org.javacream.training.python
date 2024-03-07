import socket

def start_echo_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        welcome = client_socket.recv(1024)
        name = input(welcome.decode('utf-8'))
        client_socket.sendall(name.encode('utf-8'))
        welcome = client_socket.recv(1024)
        print(welcome.decode('utf-8'))
        while True:
            message = input("Enter a Command (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode('utf-8'))

            response = client_socket.recv(1024)
            response_message = response.decode('utf-8')
            print(f"{response_message}")

if __name__ == "__main__":
    HOST = "127.0.0.1"  
    PORT = 12347

    start_echo_client(HOST, PORT)
