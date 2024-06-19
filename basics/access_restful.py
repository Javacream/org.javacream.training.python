import requests

def main():
    response = requests.get('http://javacream.eu:8080/people')
    data = response.json()
    print(data[5].get("lastname"))

main()