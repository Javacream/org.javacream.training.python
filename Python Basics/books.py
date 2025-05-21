import requests

class Book:
    def __init__(self, isbn, title, price, available):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.available = available
    def __repr__(self):
        return f'Book(isbn={self.isbn}, title={self.title}, price={self.price}, available={self.available})'

def search(isbn):
    url = f'http://javacream.eu:8080/api/books/{isbn}'
    result = requests.get(url)
    if result.status_code == 200:
        data = result.json()
        return Book(data['isbn'], data['title'], data['price'], data['available'])
    else:
        return None
