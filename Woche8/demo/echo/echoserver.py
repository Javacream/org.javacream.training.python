import socket

def start_echo_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        handle_client(client_socket)

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break  # Connection closed by the client

        message = data.decode('utf-8')
        print(f"Received message: {message}")

        # Echo the message back to the client
        client_socket.sendall(data)

    client_socket.close()
    print("Connection closed")

if __name__ == "__main__":
    HOST = "127.0.0.1"  
    PORT = 12345

    start_echo_server(HOST, PORT)
