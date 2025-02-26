import socket

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Server läuft auf {host}:{port}')
        conn, addr = s.accept()
        with conn:
            print(f'Verbunden mit {addr}')
            filename = conn.recv(1024).decode()
            print(f'Empfange Datei: {filename}')
            with open(filename, 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print('Datei empfangen und gespeichert.')

if __name__ == '__main__':
    start_server()
