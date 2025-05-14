import socket as socket_lib
def main():
    IP_ADDRESS = 'localhost' # Das ist in der Realität eine Host-Adresse
    PORT = 8000
    ENDPOINT = (IP_ADDRESS, PORT)
    with socket_lib.socket(socket_lib.AF_INET, socket_lib.SOCK_STREAM) as client_socket:
        print(f'Client Socket vor connect: {client_socket}')
        client_socket.connect(ENDPOINT)
        print(f'Client Socket nach connect: {client_socket}')

if __name__ == '__main__': 
    main()