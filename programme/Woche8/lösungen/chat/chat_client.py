import socket

def main():
    IP_ADDRESS = '127.0.0.1' # 'localhost'
    PORT = 12346
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket: 
        client_socket.connect((IP_ADDRESS, PORT))
        print(client_socket)
        name = input('Bitte Name eingeben: ')
        client_socket.sendall(name.encode('utf-8'))
        greeting = client_socket.recv(1024).decode()
        print(greeting) # Annahme: greeting enthält 'Guten Tag, {name}'
        while True:
            message = input('Bitte Nachricht eingeben: ')
            if (message == 'x'):
                break
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024).decode()
            print(response) # Annahme: '{name} schickte Nachricht {message}


if __name__ == '__main__':
    main()