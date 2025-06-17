from ipaddresses import IpAddressService

def main():
    service = IpAddressService()
    for i in range (1,5):
        service.create(f'1.2.3.{i}')
    print(f'Active addresses: {[address.ipv4_address for address in service.get_active()]}')
    print(f'Passive addresses: {[address.ipv4_address for address in service.get_passive()]}')
    service.activate('1.2.3.2')
    print(f'Active addresses: {[address.ipv4_address for address in service.get_active()]}')
    print(f'Passive addresses: {[address.ipv4_address for address in service.get_passive()]}')
if __name__ == '__main__':
    main()