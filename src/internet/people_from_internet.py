import requests

def main():
    url = 'http://javacream.eu:8080/people'
    response = requests.get(url)
    # data = response.text
    data = response.json() 
    print(data)
main()