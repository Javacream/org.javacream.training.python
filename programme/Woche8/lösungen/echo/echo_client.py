import socket
import configuration
import os
import pickle
def main():
    infile = 'requests.txt'
    outfile = 'responses.txt'
    if os.path.exists(outfile):
        os.remove(outfile)
    IP_ADDRESS, PORT = configuration.get_endpoint()
    with open(infile, 'rt', encoding='utf-8') as requests_file:
        datas = requests_file.read().split('\n')
    with open(outfile, 'at', encoding='utf-8') as responses_file:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((IP_ADDRESS, PORT))
            client_socket.sendall(pickle.dumps(datas))
            server_response = pickle.loads(client_socket.recv(1024))
            responses_file.writelines(server_response)
if __name__ == '__main__':
    main()