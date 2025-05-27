from netmiko import ConnectHandler
import keyring
def main():
    device = {
        'device_type': 'linux',
        'host': 'javacream.eu',
        'username': 'teilnehmer',
        'password': keyring.get_password("ssh_system", 'teilnehmer')
    }

    connection = ConnectHandler(**device)
    output = connection.send_command('ls')
    print(output)
main()