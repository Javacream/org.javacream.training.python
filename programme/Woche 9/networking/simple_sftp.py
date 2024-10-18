import paramiko
import keyring
def sftp_connect():
    HOST = 'javacream.eu'
    PORT = 22
    SYSTEM = 'ssh_system'
    USER = 'teilnehmer'
    PASSWORD = keyring.get_password(SYSTEM, USER)
    transport = paramiko.Transport((HOST, PORT))
    transport.connect(None, USER, PASSWORD)
    client = paramiko.SFTPClient.from_transport(transport)
    return client

def download_file(client):
    client.get('sawitzki.txt', 'from_javacream.txt')

def main():
    sftp_client =sftp_connect()
    download_file(sftp_client)
    sftp_client.close()


main()
