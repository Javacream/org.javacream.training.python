class IpAddress:
    def __init__(self, ipv4_address, type="host", status=0, dns_name=''):
        self.ipv4_address = ipv4_address
        self.type=type
        self.status = status
        self.dns_name = dns_name

class IpAddressService:
    def __init__(self):
        self.ip_addresses = dict()
        # wers mag: 
        # self.ip_addresses: dict[str, IpAddress] = dict()
    
    # wers mag: -> ist der Rückgabetyp
    # def create(ipv4_address: str) -> IpAddress
    
    def create(self, ipv4_address): 
        new_address = IpAddress(ipv4_address)
        self.ip_addresses[ipv4_address] = new_address
        return new_address
    def get_active(self):
        # 0. Leere Ergebnisliste erzeugen
        # 1. Gib mir alle Values=Werte aus dem Dictionary
        # 2. Filtere alle Values, deren Status auf 1 gesetzt ist
        # 3. Füge diese gefilterten Werte der Ergebnisliste hinzu
        # 4. Gebe diese Liste als Ergebnis zurück
        
        result = []
        addresses = self.ip_addresses.values() 
        for address in addresses:
            if address.status == 1:
                result.append(address)
        return result

    def get_passive(self):
        return [address for address in self.ip_addresses.values() if address.status == 0]

    def activate(self, ipv4_address):
        address = self.ip_addresses.get(ipv4_address)
        if address != None:
            address.status = 1 
        else:
            print(f'Aktivierung fehlgeschlagen, Adresse {ipv4_address} ist unbekannt')            
    def deactivate(self, ipv4_address):
        address = self.ip_addresses.get(ipv4_address)
        if address != None:
           address.status = 0 

    def delete(self, ipv4_address):
        address = self.ip_addresses.pop(ipv4_address, None)
        if address == None:
            print(f'Löschen fehlgeschlagen, Adresse {ipv4_address} ist unbekannt')            

