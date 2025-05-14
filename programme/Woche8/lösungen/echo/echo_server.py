import socket
from datetime import datetime
from multiprocessing import Process
import psutil
import os
def handle_request(client_socket, address_info):
    with client_socket:
        client_message = client_socket.recv(1024).decode('utf-8')
        with open ('echo.log', 'a') as log_file:
            log_file.write(f'got message from client {address_info} at {datetime.now()}: {client_message}\n')
        client_socket.sendall(f'echoing {client_message}'.encode())

def setup_shutdown(IP_ADDRESS, PORT, main_pid):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((IP_ADDRESS, PORT))
        server_socket.listen(1)
        print('waiting for shutdown')
        server_socket.accept()
        print('shutdown requested')
        main_process = psutil.Process(main_pid)
        print(f'detected main process: {main_process}')
        for sub_process in main_process.children(recursive=True):
            print(f'killing subprocess: {sub_process}')
            sub_process.kill()
        main_process.kill()    
def setup_requests(IP_ADDRESS, CLIENTS_PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((IP_ADDRESS, CLIENTS_PORT))
        server_socket.listen(1)
        while True:
            client_socket, address_info = server_socket.accept() # Hier wird die Anwendung blockiert, bis endlich eine Client-Anforderung kommt
            client_process = Process(target=handle_request, args=(client_socket, address_info)) 
            client_process.start()


def main():
    IP_ADDRESS = '127.0.0.1'
    CLIENTS_PORT = 8000 # Portnummern unter 1000 sind "reserviert" für spezielle Anwendungen, erlaubt ist alles bis hin zu 65000
    SHUTDOWN_PORT = 8001
    requests_process = Process(target=setup_requests, args=(IP_ADDRESS, CLIENTS_PORT))
    requests_process.start()
    shutdown_process = Process(target=setup_shutdown, args=(IP_ADDRESS, SHUTDOWN_PORT, os.getpid()))
    shutdown_process.start()
if __name__ == '__main__':
    main()