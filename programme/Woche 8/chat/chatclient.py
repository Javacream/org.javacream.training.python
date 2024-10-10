import socket

def main():
    # SERVER_IP_ADDRESS = '127.0.0.1' # Lokale IP, alternativ DNS: 'localhost'
    HOST = 'localhost'
    PORT = 12346 # Die Port-Nummer des Servers muss aus seiner Dokumentation entnommen werden
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT)) # ab jetzt kann der Socket als Datensenke / als Datenquelle betrachtet werden
        name = input("Bitte den Namen eingeben: ")
        client_socket.sendall(name.encode('utf-8')) # utf-8 ist bereits Standard
        greeting = client_socket.recv(1024).decode()
        print(greeting)
        while True:
            message = input("Bitte eine Nachricht eingeben: ")
            client_socket.sendall(message.encode('utf-8')) # utf-8 ist bereits Standard
            if (message == 'bye'):
                break
            response_message = client_socket.recv(1024)
            response_message = response_message.decode()
            print(f'Antwort: {response_message}')

if __name__ == '__main__':
    main()