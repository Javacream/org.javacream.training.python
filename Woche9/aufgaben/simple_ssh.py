# Aufgabe:
# Erstellen Sie einen einfachen SSH-Client, der sich zu einem SSH-Server verbinden und grundlegende Befehle ausführen kann.
# Nutzen Sie Paramiko, um eine Verbindung herzustellen, und führen Sie einfache Shell-Befehle wie ls oder pwd auf dem Server aus.

# javacream.eu - teilnehmer - javacream123!

import paramiko

# Befehl den ich absetzen möchte

command = "ls"

# Verbindungsdaten

host = "javacream.eu"
username = "teilnehmer"
password = "javacream123!"

# Verbindung aufbauen Erläuterungen zur Funktionalität: https://docs.paramiko.org/en/3.4/api/client.html

client = paramiko.client.SSHClient() # Erstellung eines SSH Clientobjekts 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Verbindung ohne einen Hostkey durchführen
client.connect(host, username=username, password=password) # Übergabe der Verbindungsparameter

# Ausführen des Befehls und wiedergabe der Ausgabe

_stdin, _stdout,_stderr = client.exec_command("ls") # Erläuterungen, siehe Ende des Skripts
print(_stdout.read().decode()) # Wiedergabe des Ouput-Streams

# Verbindung beenden
client.close()

# Code von https://www.linode.com/docs/guides/use-paramiko-python-to-ssh-into-a-server/
# stdin - der Input-Stream. Er enthält die tatsächlichen Befehle, die gesendet wurden
# stdout - der Output-Stream. Dieser enthält die Ausgabe, die das CLI als Antwort auf den Befehl zurückgibt
# stderr - hier werden alle eventuell aufgetretenen Fehler gespeichert.