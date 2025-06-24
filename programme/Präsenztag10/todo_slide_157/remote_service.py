import paramiko
import os
class RemoteService:

    def __init__(self, host, config):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, **config)
        self.ssh_client = ssh_client
        self.sftp_client = ssh_client.open_sftp()
        self.work_dir = 'python_training/27.5.2025/sawitzki'
    def upload(self, local_python_script, remote_python_script):
        try:
            self.sftp_client.mkdir(self.work_dir)
        except:
            pass # ok, work_dir exists
        self.sftp_client.chdir(self.work_dir)
        self.sftp_client.put(f'{local_python_script}', remote_python_script)
    def execute(self, remote_python_script):
        stdin, stdout, stderr = self.ssh_client.exec_command(f'python3 {self.work_dir}/{remote_python_script}')
        return (stdout.read().decode(), stderr.read().decode())

    def upload_and_execute(self, local_python_script, remote_python_script):
        self.upload(local_python_script, remote_python_script)
        return self.execute(remote_python_script)
