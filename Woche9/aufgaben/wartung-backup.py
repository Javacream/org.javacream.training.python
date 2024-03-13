# Aufgabe
# Erstellen Sie ein Skript, das regelmäßige Wartungsbefehle auf einem entfernten Server ausführt. 
# Nutzen Sie Paramiko, um sich zu einem Server zu verbinden und automatisierte Aufgaben wie Updates oder Backups durchzuführen.

# javacream.eu - teilnehmer - javacream123!

# Backup von Serverfiles in einem Ordner auf Remotehost

hostname = "javacream.eu"
port = 22
username = "teilnehmer"
password = "javacream123!"
start_directory = "/home/teilnehmer/teilnehmer/behrendt_workdir/files"
backup_dir = "/home/rainersawitzki/org.javacream.training.python/Woche9/to_backup"
remote_bck_dir = "/home/teilnehmer/teilnehmer/behrendt_workdir/backup"

import paramiko
import os
import datetime
import zipfile
import shutil

paramiko.util.log_to_file("Woche9/logs/wartung-backup.log")

def get_files_directories():

    file_list = sftp.listdir(".") # gibt eine Liste mit den Namen der Einträge im angegebenen Pfad zurück.
        
    files = []
    directories = []
    
    for file_name in file_list: 
        try:
            stat = str(sftp.lstat(file_name)) # Gibt den Status einer Datei oder eines Ordners wieder, erlaubt keine Symbolischen Links
            if stat[0] == "d":
                directories.append(file_name) # Wenn der Status gleich D, Füge der Liste directories hinzu
            elif stat[0] == "-":
                files.append(file_name) # Wenn Status gleich -, Füge der Liste files hinzu
        except PermissionError:
            print("Skipping "+file_name+" due to permissions")
            
    return files,directories
    
def backup_directory(local_dir,remote_dir):

    os.chdir(local_dir)
    sftp.chdir(remote_dir)
    print("In directory "+remote_dir)

    files,directories = get_files_directories()

    for f in files: # Lädt die Dateien aus der Liste in den neu erstellten Download (Backup) ordner herunter
        print("Backing up "+f)
        try:
            sftp.get(f, f)
        except PermissionError:
            print("Skipping "+f+" due to permissions")

        
    for d in directories: # Lädt den aktuellen Ordner aus der directories Liste stellt die Downloadordnervariable auf diesen um. Die Funktion für den Directory Backup wird erneut aufgerufen
        newremote = remote_dir+d+"/"
        newlocal = local_dir+"\\"+d
        os.mkdir(newlocal)
        backup_directory(newlocal,newremote)
        
def zipfolder (foldername, target_dir):
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])

def upload_bck ():
    # Suche alle Dateien im Backupverzeichnis die mit .zip Enden
    for file in os.listdir(backup_dir):
        if file.endswith(".zip"):
            backupzip = file
    
    # Angabe der Start und Zieldatei. Ersetzen der "falschen" übersetzung von \\
    connected_path_local_bck = os.path.join(backup_dir, backupzip).replace("\\","/")
    connected_path_remote_bck = os.path.join(remote_bck_dir, backupzip).replace("\\","/")

    # Upload der Datei
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(connected_path_local_bck,connected_path_remote_bck)
    sftp.close()

def cleanup ():
    folder = backup_dir
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename).replace("\\","/")
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

os.chdir(backup_dir)

# Erstellt einen Ordner mit aktuellem Datum

datestring = str(datetime.date.today())

os.mkdir(datestring)
os.chdir(datestring)
local_dir = os.getcwd()

# Verbindung zum Server

transport = paramiko.Transport((hostname, port))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Backup aller Dateien im festgelegtem Ordner

remote_dir = start_directory
backup_directory(local_dir,remote_dir)

# SFTP Verbindungen schließen

sftp.close()

# Lokale Sicherung des Remoteservers zippen, upload der Backupdatei und löschen lokaler kopien

zipfolder (local_dir, local_dir)
upload_bck ()
cleanup ()

# Transport Verbindungen schließen

transport.close()