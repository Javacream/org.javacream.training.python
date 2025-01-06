import socket

def main():
    IP_ADDRESS = '127.0.0.1' # 'localhost'
    PORT = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket: # client_socket ist nur eine leere Hülle!
        client_socket.connect((IP_ADDRESS, PORT)) # ab jetzt ist der Socket real
if __name__ == '__main__':
    main()