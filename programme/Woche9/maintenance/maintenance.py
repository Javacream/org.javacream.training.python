import paramiko
import sys
import keyring

zip_file = './content.zip'
zip_creator_file = './zip_creator.py'
remote_path = 'python_training/4.12.2025/sawitzki'
local_path = 'programme/Woche9/maintenance'
def ssh_connect():
    ssh_client = paramiko.client.SSHClient()
    HOST = 'javacream.eu'
    PORT = 22
    USER = 'teilnehmer'
    PASSWORD = keyring.get_password('TRAINING', USER)
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(HOST, port=PORT, username=USER, password=PASSWORD)
    sftp_client:paramiko.SFTPClient = ssh_client.open_sftp()
    return (ssh_client, sftp_client)

def prepare_directories(sftp_client:paramiko.SFTPClient):
    sftp_client.chdir(remote_path)

def upload_zip_creator(sftp_client:paramiko.SFTPClient):
    if zip_creator_file in sftp_client.listdir():
        sftp_client.remove(zip_creator_file)
    sftp_client.put(f'{local_path}/{zip_creator_file}', zip_creator_file)

def download_zip(sftp_client:paramiko.SFTPClient):
    sftp_client.get(zip_file, zip_file)

def start_zip_creator(ssh:paramiko.SSHClient):
    stdin, stdout, stderr = ssh.exec_command(f'cd {remote_path}; python3 {zip_creator_file}')
    return (stdout.read().decode(), stderr.read().decode())

def clean_up(sftp_client):
    sftp_client.remove(zip_creator_file)
    sftp_client.remove(zip_file)

def main():
    ssh, sftp = ssh_connect()
    prepare_directories(sftp)
    upload_zip_creator(sftp)
    print(start_zip_creator(ssh))
    download_zip(sftp)
    clean_up(sftp)
    sftp.close()
    ssh.close()
if __name__ == "__main__":
    main()
