import requests
class NautobotService:
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.headers = {
            'Authorization': f'Token {token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }


    def get_ip_addresses(self):
        response = requests.get(f'{self.endpoint}ipam/ip-addresses/', headers=self.headers)
        ip_addresses = response.json()
        return ip_addresses.get('results', [])
     
