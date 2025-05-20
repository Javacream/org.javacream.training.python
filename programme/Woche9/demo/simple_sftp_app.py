import paramiko
import keyring
def sftp_connect():
    HOST = 'javacream.eu'
    PORT = 22
    SYSTEM = 'TRAINING'
    USER = 'teilnehmer'
    PASSWORD = keyring.get_password(SYSTEM, USER)
    transport = paramiko.Transport((HOST, PORT))
    transport.connect(None, USER, PASSWORD)
    client = paramiko.SFTPClient.from_transport(transport)
    return client

def prepare(client:paramiko.SFTPClient):
    client.chdir('python_training')
    folder_name = 'sawitzki'
    if folder_name not in client.listdir('.'):      
        client.mkdir(folder_name)
    client.chdir(folder_name)    

def upload(client:paramiko.SFTPClient):
    client.put('README.md', 'README.md')

def main():
    sftp_client = sftp_connect()
    prepare(sftp_client)
    upload(sftp_client)
    sftp_client.close()


main()
