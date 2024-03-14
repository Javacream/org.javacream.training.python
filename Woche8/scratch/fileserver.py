# Aufgabe:
# Entwickeln Sie eine Anwendung, die das Hoch- und Herunterladen von Dateien zwischen einem Client und einem Server ermöglicht. 
# Implementieren Sie sowohl Server- als auch Client-Seite, die es erlauben, Dateien in beide Richtungen zu übertragen.
# Part: File Server

import socket
import os
import os.path

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432

# Erhalte immer 4096 bytes
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# Server socket erstellen (TCP)
server_socket = socket.socket()

# Socket an lokale Adresse binden
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Server erlauben Verbindungen anzunehmen.
# 5 ist die Anzahl der nicht akzeptierten Verbindungen, die das System zulässt, bevor es neue Verbindungen ablehnt
server_socket.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# Verbindungen erlauben
client_socket, address = server_socket.accept() 
# Wenn der Text ausgegeben wird, ist die Verbindung zustande gekommen
print(f"[+] {address} is connected.")

# Erhalte Datei-Informationen
# Erhalten der Datei via Client Socket
received = client_socket.recv(BUFFER_SIZE).decode("utf-8")
client_socket.sendall("OK".encode())
uploadfilename, filesizeup = received.split(SEPARATOR)

# Absoluten Pfad entfernen falls vorhanden
uploadfilename = os.path.basename(uploadfilename)

# Konvertierung in Integer
filesizeup = int(filesizeup)

# Pfad unter dem die Datei hochgeladen werden soll
upload_path = "tmp/Serverdaten"
complete_uf_name = os.path.join(upload_path, uploadfilename)

# Empfangen der Datei vom Socket und das Schreiben in den file stream
with open(complete_uf_name, "wb") as uf:
    while True:
        # 1024 bytes vom socket
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # Nichts erhalten
            # Dateiübertragung fertig
            break
        # Die erhaltenen bytes als Datei schreiben
        uf.write(bytes_read)

# client socket schließen
client_socket.close()
# server socket schließen
server_socket.close()

# Upload-Code von https://thepythoncode.com/article/send-receive-files-using-sockets-python