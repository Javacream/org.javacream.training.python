import requests
class BooksService:
    def __init__(self):
        self.url = 'http://javacream.eu:8081/api/books'
    def search_by(self, isbn):
        url = f'{self.url}/{isbn}'
        data = requests.get(url).json()
        book = Book(data)
        return book
    def find_all(self):
        url = self.url
        datas = requests.get(url).json()
        result = []
        for data in datas:
            book = Book(data)
            result.append(book)
        return result

class Book:
    def __init__(self, book_data_dict):
        self.isbn = book_data_dict['isbn']
        self.title = book_data_dict['title']
        self.price = book_data_dict['price']
        self.available = book_data_dict['available']
    def __repr__(self):
        return f'Book(isbn={self.isbn}, title={self.title}, price={self.price}, available={self.available})'