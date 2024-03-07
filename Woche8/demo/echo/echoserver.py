import socket

def start_echo_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")
        client_socket, address = server_socket.accept()
        with client_socket:
            print(f"Accepted connection from {client_socket}")
            while True:
                handle_client(client_socket)

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break  # Connection closed by the client
        message = data.decode('utf-8')
        print(f"Received message: {message} from {client_socket}")
        # Echo the message back to the client
        client_socket.sendall(data)

if __name__ == "__main__":
    HOST = "localhost"  
    PORT = 12345

    start_echo_server(HOST, PORT)
