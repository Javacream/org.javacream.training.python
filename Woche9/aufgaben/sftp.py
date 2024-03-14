# Aufgabe
# Entwickeln Sie einen Client, der Dateien über SFTP übertragen kann. 
# Implementieren Sie Funktionen zum Hochladen und Herunterladen von Dateien. Experimentieren Sie mit verschiedenen Dateitypen und -größen.

# javacream.eu - teilnehmer - javacream123!

import paramiko

paramiko.util.log_to_file("Woche9/logs/sftp.log")

# Öffnet einen Transport # https://docs.paramiko.org/en/latest/api/transport.html
host,port = "javacream.eu",22
transport = paramiko.Transport((host,port))

# Authentifizierung   
username,password = "teilnehmer","javacream123!"
transport.connect(None,username,password)

# Erstellt einen SFTP Client Channel
sftp = paramiko.SFTPClient.from_transport(transport)

# Downloadfunktion
filepath = "/home/teilnehmer/teilnehmer/behrendt_workdir/files/downloadfile_behrendt.txt"
localpath = "Woche9/downloadfile_behrendt.txt"
sftp.get(filepath,localpath)

# Uploadfunktion
filepath = "/home/teilnehmer/teilnehmer/behrendt_workdir/files/s1.txt"
localpath = "Woche9/aufgaben/sawitzki.txt"
sftp.put(localpath,filepath)

# Verbindung beenden
if sftp: sftp.close()
if transport: transport.close()

# Code von https://stackoverflow.com/questions/3635131/paramikos-sshclient-with-sftp