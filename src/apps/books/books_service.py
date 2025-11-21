import requests
class BooksService:
    def __init__(self):
        self.url = 'http://javacream.eu:8081/api/books'
    def search_by(self, isbn):
        url = f'{self.url}/{isbn}'
        return requests.get(url).json()
    def find_all(self):
        pass