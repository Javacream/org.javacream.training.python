import requests

def search_by(isbn):
    url = f'http://javacream.eu:8081/api/books/{isbn}'
    return requests.get(url).json()
