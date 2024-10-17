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
    remote_stdin, remote_stdout, remote_stderr = client.exec_command(cmd) # r_stdin, r_stdout, r_stderr = client.exec
    remote_stdout.channel.recv_exit_status()
    result = remote_stdout.read().decode()
    error = remote_stderr.read().decode()
    if result:
        return result
    else:
        raise Exception(error)

def ls(client):
    result = ssh_execute_command(client, 'ls')
    print(result)

def long_ls(client):
    result = ssh_execute_command(client, 'ls -l')
    print(result)

def wrong_ls(client):
    try:
        result = ssh_execute_command(client, 'ls-l')
        print(result)
    except Exception as e:
        print(e)


def main():
    client = ssh_connect()
    ls(client)
    long_ls(client)
    wrong_ls(client)
    client.close()

main()
