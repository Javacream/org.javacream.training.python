import socket

def main():
    # SERVER_IP_ADDRESS = '127.0.0.1' # Lokale IP, alternativ DNS: 'localhost'
    HOST = '127.0.0.1'
    PORT = 12345 # Die Port-Nummer des Servers muss aus seiner Dokumentation entnommen werden
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT)) # ab jetzt kann der Socket als Datensenke / als Datenquelle betrachtet werden

if __name__ == '__main__':
    main()