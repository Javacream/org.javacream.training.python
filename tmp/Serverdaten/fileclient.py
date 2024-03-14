# Aufgabe:
# Entwickeln Sie eine Anwendung, die das Hoch- und Herunterladen von Dateien zwischen einem Client und einem Server ermöglicht. 
# Implementieren Sie sowohl Server- als auch Client-Seite, die es erlauben, Dateien in beide Richtungen zu übertragen.
# Part: File Client

import socket
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # 4096 Bytes pro time step senden

host = "127.0.0.1"
port = 65432
uploadfilename = "Woche8/scratch/fileclient.py" # File das an den Server gesendet werden soll

# Dateigröße auslesen
filesizeup = os.path.getsize(uploadfilename)

# client socket erstellen
client_socket = socket.socket()

# Verbinden zum Server
print(f"[+] Connecting to {host}:{port}")
client_socket.connect((host, port))
print("[+] Connected.")

# Dateiname und größe senden
client_socket.send(f"{uploadfilename}{SEPARATOR}{filesizeup}\n".encode("utf-8"))
client_socket.recv(BUFFER_SIZE)
with open(uploadfilename, "rb") as uf:
    while True:
        # Bytes der Datei lesen
        bytes_read = uf.read(BUFFER_SIZE)
        if not bytes_read:
            # Dateitransfer fertig
            break
        # sendall wird benutzt um den Dateitransfer auch in ausgelasteten Netzwerken sicher zu stellen 
        client_socket.sendall(bytes_read)

# close the socket
client_socket.close()

# Code von https://thepythoncode.com/article/send-receive-files-using-sockets-python