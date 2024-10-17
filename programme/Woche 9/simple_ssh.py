import paramiko
import paramiko.client


client = paramiko.client.SSHClient()

HOST = 'javacream.eu'
PORT = 22
USER = 'teilnehmer'
PASSWORD = 'javacream123!'
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, port=PORT, username=USER, password=PASSWORD) # Nach Ausführung von Connect wird auf javacream.eu ein Shell-Prozess gestartet

remote_process = client.exec_command('ls') # r_stdin, r_stdout, r_stderr = client.exec
remote_stdout = remote_process[1]
result = remote_stdout.read().decode()
print(result)
client.close()