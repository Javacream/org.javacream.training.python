import paramiko
import paramiko.client

def ssh_connect():
    client = paramiko.client.SSHClient()
    HOST = 'javacream.eu'
    PORT = 22
    USER = 'teilnehmer'
    PASSWORD = 'javacream123!'
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, port=PORT, username=USER, password=PASSWORD) # Nach Ausführung von Connect wird auf javacream.eu ein Shell-Prozess gestartet
    return client

def ssh_execute_command(client, cmd):
    remote_process = client.exec_command(cmd) # r_stdin, r_stdout, r_stderr = client.exec
    remote_stdout = remote_process[1]
    result = remote_stdout.read().decode()
    return result

def main():
    client = ssh_connect()
    result = ssh_execute_command(client, 'ls')
    print(result)

main()
