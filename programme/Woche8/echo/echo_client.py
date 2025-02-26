import socket
def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8000 # Portnummern unter 1000 sind "reserviert" für spezielle Anwendungen, erlaubt ist alles bis hin zu 65000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print(f'Client Socket vor connect: {client_socket}')
        client_socket.connect((IP_ADDRESS, PORT))
        print(f'Client Socket nach connect: {client_socket}')

if __name__ == '__main__':
    main()