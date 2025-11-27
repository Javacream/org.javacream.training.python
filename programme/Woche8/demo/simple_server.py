import socket

def main():
    IP_ADDRESS = '127.0.0.1' #'localhost'
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        print(server_socket)
        server_socket.bind((IP_ADDRESS, PORT))
        server_socket.listen(1)
        print(server_socket)
        socket_for_client, address_info = server_socket.accept() # das ist ein blockierender Vorgang
        print(socket_for_client)
        message = socket_for_client.recv(1024).decode('utf-8')
        print(message)
main()