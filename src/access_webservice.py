import requests # Keine Standard-Bibliothek, installieren mit pip install requests

def main():
    #api_url = "https://jsonplaceholder.typicode.com/todos/1"
    api_url = 'http://javacream.eu:8080/api/books'
    response = requests.get(api_url)
    json_result = response.json()
    print(json_result[0]['isbn'])
main()