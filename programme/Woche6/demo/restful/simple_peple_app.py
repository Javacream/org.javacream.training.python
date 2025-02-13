import requests

def main():
    endpoint = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(endpoint)
    if response.ok:
        data = response.json()
        print(data)
    else:
        print(f'Fehler beim Zugriff: {response.status_code}')
if __name__ == '__main__':
    main()