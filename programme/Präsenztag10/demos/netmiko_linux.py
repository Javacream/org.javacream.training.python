from netmiko import ConnectHandler
def main():
    device = {
        'device_type': 'linux',
        'host': 'javacream.eu',
        'username': 'teilnehmer',
        'password': 'javacream123!'
    }

    connection = ConnectHandler(**device)
    output = connection.send_command('ls')
    print(output)
main()