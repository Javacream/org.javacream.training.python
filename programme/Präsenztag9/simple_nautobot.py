import requests

NAUTOBOT_URL = 'https://demo.nautobot.com/api/'
API_TOKEN = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

headers = {
    'Authorization': f'Token {API_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

def get_ip_addresses():
    response = requests.get(f'{NAUTOBOT_URL}ipam/ip-addresses/', headers=headers)
    ip_addresses = response.json()

    for ip in ip_addresses.get('results', []):
        print(f"IP: {ip['address']}")


def main():
    get_ip_addresses()

if __name__ == '__main__':
    main()