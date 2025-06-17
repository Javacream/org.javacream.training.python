from ipaddresses import IpAddressService

def main():
    service = IpAddressService()
    for i in range (1,5):
        service.create(f'1.2.3.{i}')

    for address in service.get_active():
        print(address.ipv4_address)
    print(f'Passive addresses: {[address.ipv4_address for address in service.get_passive()]}')

    service.activate('1.2.3.2')

    for address in service.get_active():
        print(address.ipv4_address)
    print(f'Passive addresses: {[address.ipv4_address for address in service.get_passive()]}')

if __name__ == '__main__':
    main()