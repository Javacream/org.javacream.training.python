import requests
from statistics import mean

class BooksService:
    def __init__(self):
        self.ENDPOINT = 'http://javacream.eu:8081/api/books'
    def read_all(self):
        return requests.get(self.ENDPOINT).json()
    def min_price(self, books):
        return min([b['price'] for b in books])
    def max_price(self, books):
        return max([b['price'] for b in books])
    def avg_price(self, books):
        return mean([b['price'] for b in books])
    def create(self, title):
        response = requests.post(f'{self.ENDPOINT}/{title}')
        if response.ok:
            return response.text
        else:
            return f'Error: {response.status_code}'
    def update_price(self, isbn, new_price):
        response = requests.get(f'{self.ENDPOINT}/{isbn}')
        if response.ok:
            book = response.json()
            book['price'] = new_price
            put_response = requests.put(f'{self.ENDPOINT}/{isbn}', json=book)
            if not put_response.ok:
                print(f'Error while updating {isbn}: {put_response.status_code}')
    def find_by_isbn(self, isbn):
        return requests.get(f'{self.ENDPOINT}/{isbn}').json()
    def delete_by_isbn(self, isbn):
        response = requests.delete(f'{self.ENDPOINT}/{isbn}')
        if not response.ok:
            print(f'Error deleting isbn {isbn}: {response.status_code}')
