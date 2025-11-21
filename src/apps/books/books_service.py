import requests
class BooksService:
    def search_by(self, isbn):
        url = f'http://javacream.eu:8081/api/books/{isbn}'
        return requests.get(url).json()
