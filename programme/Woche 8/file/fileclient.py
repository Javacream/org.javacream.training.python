import socket
import os

def send_file(filename, host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f'Verbunden mit {host}:{port}')
        s.sendall(os.path.basename(filename).encode())
        with open(filename, 'rb') as f:
            print(f'Sende Datei: {filename}')
            while True:
                data = f.read(1024)
                if not data:
                    break
                s.sendall(data)
        print('Datei erfolgreich gesendet.')

if __name__ == '__main__':
    file_to_send = 'deine_datei.txt'  # Ändere dies auf den Pfad deiner Datei
    send_file(file_to_send)
