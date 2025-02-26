import socket

def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8000 # Portnummern unter 1000 sind "reserviert" für spezielle Anwendungen, erlaubt ist alles bis hin zu 65000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((IP_ADDRESS, PORT))
        server_socket.listen(1)
        while True:
            client_socket, address_info = server_socket.accept() # Hier wird die Anwendung blockiert, bis endlich eine Client-Anforderung kommt
            print(f'Client-Socket: {client_socket}, Address-Info: {address_info}')
            message_from_client = client_socket.recv(1024).decode('utf-8')
            print(f'Message={message_from_client}')
            client_socket.sendall('OK'.encode())
if __name__ == '__main__':
    main()