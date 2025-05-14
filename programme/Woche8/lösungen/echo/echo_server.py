import socket
from datetime import datetime
def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8000 # Portnummern unter 1000 sind "reserviert" für spezielle Anwendungen, erlaubt ist alles bis hin zu 65000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((IP_ADDRESS, PORT))
        server_socket.listen(1)
        while True:
            client_socket, address_info = server_socket.accept() # Hier wird die Anwendung blockiert, bis endlich eine Client-Anforderung kommt
            with client_socket:
                client_message = client_socket.recv(1024).decode('utf-8')
                if client_message == 'secret_stop_code':
                    print("received stop message, exiting...")
                    break
                with open ('echo.log', 'a') as log_file:
                    log_file.write(f'got message from client {address_info} at {datetime.now()}: {client_message}\n')
                client_socket.sendall(f'echoing {client_message}'.encode())
if __name__ == '__main__':
    main()