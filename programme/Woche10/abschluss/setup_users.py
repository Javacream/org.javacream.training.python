import paramiko
from credentials import get_password
from setup_utilities import *
class UsersSetup:
    def init(self, configuration):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            host = configuration['remote']['host']
            port = configuration['remote']['port']
            username = configuration['credentials']['username']
            ssh.connect(host, port=port, username=username, password=get_password(configuration['credentials']))
            self.ssh = ssh
            self.basedir = configuration['remote']['basedir']
        except paramiko.SSHException as e:
            print(f"SSH-Fehler: {e}")
        except Exception as e:
            print(f"Allgemeiner Fehler: {e}")
    def close(self):
        self.ssh.close()            
    def setup(self):
        directories = directories_from_path(self.basedir)
        try:
            self.ssh.exec_command(f'rm -rf {directories[0]}')
        except Exception as e:
            print(f'Fehler beim Löschen von {self.basedir}: {e}')
        try:
            for directory in directories:
                self.ssh.exec_command(f'mkdir {directory}')
        except Exception as e:
            print(f'Fehler beim Anlegen von {self.basedir}: {e}')

    def create_remote_directories(self, people_json):
        remote_directories = names_from_people_list(people_json)
        try:
            index = 0
            while index < len(people_json):
                remote_directory = remote_directories[index]
                self.ssh.exec_command(f'mkdir {self.basedir}/{remote_directory}')
                self.ssh.exec_command(f'echo {people_json[index]} > {self.basedir}/{remote_directory}/user.json')
                index += 1
        except IOError as e:
            print(f"Fehler beim Erstellen der Verzeichnisse: {e}")

