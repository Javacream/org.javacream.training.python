from netmiko import ConnectHandler
import keyring
def main():
    device = {
        'device_type': 'cisco_ios',
        'host': '192.168.111.110',
        'username': 'admin',
        'password': keyring.get_password("cisco", 'admin')
    }

    connection = ConnectHandler(**device)
    output = connection.send_command('show version')
    print(output)
main()