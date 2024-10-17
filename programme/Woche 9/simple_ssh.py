import paramiko
import paramiko.client


client = paramiko.client.SSHClient()

HOST = 'javacream.eu'
PORT = 22
USER = 'teilnehmer'
PASSWORD = 'javacream123!'
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, port=PORT, username=USER, password=PASSWORD)