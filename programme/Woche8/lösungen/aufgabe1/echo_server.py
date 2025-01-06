import socket 
def main():
    IP_ADDRESS = '127.0.0.1' # 'localhost' oder das Ergebnis von ipconfig (Windows) ip -A
    PORT = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((IP_ADDRESS, PORT))
        server_sock.listen(1)
        server_sock.accept()

if __name__ == '__main__':
    main()