from netmiko import ConnectHandler
def main():
    device = {
        'device_type': 'cisco',
        'host': '192.188.160.120',
        'username': 'hugo',
        'password': 'emil!'
    }

    connection = ConnectHandler(**device)
    output = connection.send_command('show version')
    print(output)
main()