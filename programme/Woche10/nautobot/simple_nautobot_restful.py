import requests

def main():
    NAUTOBOT_ENDPOINT = 'https://demo.nautobot.com/api'
    API_TOKEN = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    headers = {
        'Authorization': f'Token {API_TOKEN}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'

    }
    response = requests.get(f'{NAUTOBOT_ENDPOINT}/ipam/ip-addresses/', headers=headers)
    data = response.json()
    ip_addresses = data['results']
    print(f'done, read {data["count"]} rows')
if __name__ == '__main__':
    main()