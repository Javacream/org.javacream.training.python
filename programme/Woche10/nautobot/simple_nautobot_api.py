from pynautobot import api

# Konfigurationsparameter
NAUTOBOT_URL = 'https://demo.nautobot.com'
API_TOKEN = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

def main():
    nautobot_client = api(url=NAUTOBOT_URL, token=API_TOKEN)
    print(nautobot_client.dcim)

if __name__ == '__main__': main()