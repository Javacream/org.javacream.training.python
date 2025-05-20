import paramiko
import keyring
def ssh_connect():
    HOST = 'javacream.eu'
    PORT = 22
    SYSTEM = 'TRAINING'
    USER = 'teilnehmer'
    PASSWORD = keyring.get_password(SYSTEM, USER)
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, port=PORT, username=USER, password=PASSWORD) # Nach Ausführung von Connect wird auf javacream.eu ein Shell-Prozess gestartet
    return client

def upload_backup_script(client:paramiko.SSHClient):
    sftp_client = client.open_sftp()
    sftp_client.chdir('python_training/sawitzki')
    sftp_client.put('programme/Woche9/demo/backup_app.py', 'backup_app.py')

def exec_backup_script(client:paramiko.SSHClient):
    stdin, stdout, stderr = client.exec_command('cd python_training/sawitzki; python3 backup_app.py')
    potential_error = stderr.read().decode()
    if  potential_error != '':
        raise Exception(potential_error)

def download_zip(client:paramiko.SSHClient):
    sftp_client = client.open_sftp()
    sftp_client.chdir('python_training/sawitzki')
    sftp_client.get('backup.zip', 'backup.zip')

def main():
    ssh_client = ssh_connect()
    upload_backup_script(ssh_client)
    exec_backup_script(ssh_client)
    download_zip(ssh_client)
    ssh_client.close()


main()
