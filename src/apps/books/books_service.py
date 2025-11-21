import requests
class Book:
    def __init__(self, book_data_dict: dict):
        self.isbn: str = book_data_dict['isbn']
        self.title: str = book_data_dict['title']
        self.price: float = book_data_dict['price']
        self.available: bool = book_data_dict['available']
    def __repr__(self):
        return f'Book(isbn={self.isbn}, title={self.title}, price={self.price}, available={self.available})'
class BooksService:
    def __init__(self):
        self.url = 'http://javacream.eu:8081/api/books'
    def search_by(self, isbn: str) -> Book:
        url = f'{self.url}/{isbn}'
        data = requests.get(url).json()
        book = Book(data)
        return book
    def find_all(self) -> list[Book]:
        url = self.url
        datas = requests.get(url).json()
        return [Book(data) for data in datas]
