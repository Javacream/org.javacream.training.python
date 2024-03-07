import socket

def start_echo_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        while True:
            message = input("Enter a message (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode('utf-8'))

            data = client_socket.recv(1024)
            echoed_message = data.decode('utf-8')
            print(f"Server echoed: {echoed_message}")

if __name__ == "__main__":
    HOST = "127.0.0.1"  
    PORT = 12345

    start_echo_client(HOST, PORT)
