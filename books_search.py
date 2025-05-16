import requests
def search(isbn):
    url = f'http://javacream.eu:8080/api/books/{isbn}'
    result = requests.get(url)
    if result.status_code == 200:
        data = result.json()
        return (data['title'], data['price'])
    else:
        return ()
