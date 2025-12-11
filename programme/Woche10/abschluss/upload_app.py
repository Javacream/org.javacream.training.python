from configuration import read_configuration
from credentials import get_password
import paramiko
def main():
    try:
        configuration = read_configuration('programme/Woche10/upload_configuration.json')
        name = input ('Bitte geben Sie Ihren Namen an: <Vorname> <Nachname>: ')
        name = name.replace(' ', '.')
        filename = input('Welche Datei soll hochgeladen werden? ')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        host = configuration['remote']['host']
        port = configuration['remote']['port']
        username = configuration['credentials']['username']
        ssh.connect(host, port=port, username=username, password=get_password(configuration['credentials']))
        sftp = ssh.open_sftp()
        sftp.put(filename, f"{configuration['remote']['basedir']}/{name}/{filename}")
    except FileNotFoundError as e:
        print(f'Error transferring {filename} to {configuration['remote']['basedir']}/{name}/{filename}: {e}')
    except paramiko.SSHException as e:
        print(f'SSH error: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        ssh.close()


if __name__ == '__main__':
    main()