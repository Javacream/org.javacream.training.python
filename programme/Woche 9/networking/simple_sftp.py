import paramiko

def sftp_connect():
    HOST = 'javacream.eu'
    PORT = 22
    USER = 'teilnehmer'
    PASSWORD = 'javacream123!'
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
