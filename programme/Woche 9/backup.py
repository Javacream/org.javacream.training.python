hostname = "javacream.eu"
port = 22
username = "teilnehmer"
password = "javacream123!"
start_directory = "..."
backup_dir = "..."
remote_bck_dir = "/home/teilnehmer/backup"

import paramiko
import os
import datetime
import zipfile
import shutil


def get_files_directories():

    file_list = sftp.listdir(".")
        
    files = []
    directories = []
    
    for file_name in file_list: 
        try:
            stat = str(sftp.lstat(file_name))
            if stat[0] == "d":
                directories.append(file_name)
            elif stat[0] == "-":
                files.append(file_name) 
        except PermissionError:
            print("Skipping "+file_name+" due to permissions")
            
    return files,directories
    
def backup_directory(local_dir,remote_dir):

    os.chdir(local_dir)
    sftp.chdir(remote_dir)
    print("In directory "+remote_dir)

    files,directories = get_files_directories()

    for f in files: 
        print("Backing up "+f)
        try:
            sftp.get(f, f)
        except PermissionError:
            print("Skipping "+f+" due to permissions")

        
    for d in directories: 
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
    for file in os.listdir(backup_dir):
        if file.endswith(".zip"):
            backupzip = file
    
    connected_path_local_bck = os.path.join(backup_dir, backupzip).replace("\\","/")
    connected_path_remote_bck = os.path.join(remote_bck_dir, backupzip).replace("\\","/")

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
datestring = str(datetime.date.today())
os.mkdir(datestring)
os.chdir(datestring)
local_dir = os.getcwd()


transport = paramiko.Transport((hostname, port))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)


remote_dir = start_directory
backup_directory(local_dir,remote_dir)


sftp.close()
zipfolder (local_dir, local_dir)
upload_bck ()
cleanup ()


transport.close()
