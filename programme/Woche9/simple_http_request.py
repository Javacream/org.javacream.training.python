import requests
def main():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    if response.ok:
        data = response.json()
        print(data)
    print(data)
if __name__ == '__main__': main()