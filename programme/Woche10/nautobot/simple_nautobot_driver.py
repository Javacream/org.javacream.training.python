from pynautobot import api

# Konfigurationsparameter
NAUTOBOT_URL = 'https://demo.nautobot.com'
API_TOKEN = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

def main():
    nautobot_client = api(url=NAUTOBOT_URL, token=API_TOKEN)
    ipam = nautobot_client.ipam
    ip_addresses = ipam.ip_addresses.all()
    print(len(ip_addresses))

if __name__ == '__main__': main()