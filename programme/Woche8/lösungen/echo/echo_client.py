import socket
import configuration
import os
def main():
    infile = 'requests.txt'
    outfile = 'responses.txt'
    if os.path.exists(outfile):
        os.remove(outfile)
    IP_ADDRESS, PORT = configuration.get_endpoint()
    with open(infile, 'rt', encoding='utf-8') as requests_file:
        datas = requests_file.read().split('\n')
    with open(outfile, 'at', encoding='utf-8') as responses_file:
        for data in datas:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((IP_ADDRESS, PORT))
                client_socket.sendall(data.encode('utf-8'))
                server_response = client_socket.recv(1024).decode()
                responses_file.write(f'{server_response}\n')
if __name__ == '__main__':
    main()