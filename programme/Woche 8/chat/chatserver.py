import socket
import multiprocessing as mp
import pickle
import os.path
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
            process = mp.Process(target=handle_client, args=(client_socket, ))
            process.start()

def handle_client(client_socket):
        with client_socket:
            name = client_message = client_socket.recv(1024).decode()
            if os.path.isfile(name):
                with open(name, 'rb') as file:
                    messages = pickle.load(file)
            else:
                messages = []
            if len(messages) > 0:
                last_message = messages[-1]
            else:
                last_message = "not available"        
            client_socket.sendall(f'Hello {name}, you have {len(messages)} chat entries, last message is {last_message}\n'.encode())
            while True:
                client_message = client_socket.recv(1024).decode()
                print(f'Received message: {client_message}')
                if client_message == 'bye':
                    print(f'terminating client connection {client_socket}')
                    break
                messages.append(client_message)
                with open (name, 'wb') as file:
                    pickle.dump(messages, file)
                client_socket.sendall(f'{name} deine Nachricht war {client_message}\n'.encode())

if __name__ == '__main__':
    main()