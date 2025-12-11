from netmiko import ConnectHandler
import keyring
def main():
    device = {
        'device_type': 'cisco_ios',
        'host': 'https://sandboxapicdc.cisco.com',
        'username': 'admin',
        'password': '!v3G@!4@Y'
    }

    connection = ConnectHandler(**device)
    output = connection.send_command('show version')
    print(output)
main()