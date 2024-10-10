import socket


def main():
    # HOST = 'localhost' # Dieser Host nimmt nur Anfragen von localhost entgegen, er bindet nur auf localhost
    # HOST = '192.168.178.76' # Der Hoszt nimmt so alle Anfragen entgegen, die an diese IP-Adresse gerichtet sind
    HOST = '0.0.0.0' # Zum Testen sehr einfach, bindet an alle IP-Adressen des aktuellen Rechners, etwas "Quick and Dirty" 
    PORT = 12346 # Die Port-Nummer des Servers muss aus seiner Dokumentation entnommen werden
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(0)
        print(f'Server listening on {HOST} {PORT}')
        while True:
            client_socket, address = server_socket.accept() # Blockierendes Warten auf einen Client-Request
            print(f'Accepted client connection: {client_socket}')
            handle_client(client_socket)

def handle_client(client_socket):
        with client_socket:
            name = client_message = client_socket.recv(1024).decode()
            client_socket.sendall(f'Hello {name}\n'.encode())
            while True:
                client_message = client_socket.recv(1024).decode()
                print(f'Received message: {client_message}')
                if (client_message == 'bye'):
                    print(f'terminating client connection {client_socket}')
                    break
                client_socket.sendall(f'{name} deine Nachricht war {client_message}\n'.encode())

if __name__ == '__main__':
    main()