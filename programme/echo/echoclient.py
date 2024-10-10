import socket

def main():
    # SERVER_IP_ADDRESS = '127.0.0.1' # Lokale IP, alternativ DNS: 'localhost'
    HOST = 'javacream.eu'
    PORT = 12345 # Die Port-Nummer des Servers muss aus seiner Dokumentation entnommen werden
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT)) # ab jetzt kann der Socket als Datensenke / als Datenquelle betrachtet werden
        message = "Hello\n"
        client_socket.sendall(message.encode('utf-8')) # utf-8 ist bereits Standard
        response_message = client_socket.recv(1024)
        response_message = response_message.decode()
        print(f'Server response: {response_message}')

if __name__ == '__main__':
    main()