import socket

def handle_client_request(client_socket):
        with client_socket:
            message_from_client = client_socket.recv(1024).decode('utf-8')
            print(f'got message from client: {message_from_client}')
            client_socket.sendall('OK'.encode())

def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8000 # Portnummern unter 1000 sind "reserviert" für spezielle Anwendungen, erlaubt ist alles bis hin zu 65000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((IP_ADDRESS, PORT))
        server_socket.listen(1)
        while True:
            client_socket, address_info = server_socket.accept() # Hier wird die Anwendung blockiert, bis endlich eine Client-Anforderung kommt
            handle_client_request(client_socket)
if __name__ == '__main__':
    main()