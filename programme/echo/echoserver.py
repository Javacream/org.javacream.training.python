import socket


def main():
    # HOST = 'localhost' # Dieser Host nimmt nur Anfragen von localhost entgegen, er bindet nur auf localhost
    # HOST = '192.168.178.76' # Der Hoszt nimmt so alle Anfragen entgegen, die an diese IP-Adresse gerichtet sind
    HOST = '0.0.0.0' # Zum Testen sehr einfach, bindet an alle IP-Adressen des aktuellen Rechners, etwas "Quick and Dirty" 
    PORT = 12345 # Die Port-Nummer des Servers muss aus seiner Dokumentation entnommen werden
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f'Server listening on {HOST} {PORT}')

if __name__ == '__main__':
    main()