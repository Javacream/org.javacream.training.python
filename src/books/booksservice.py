import requests


class Book:
    def __init__(self, isbn, title, price):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.available = False
    def info(self):
        return "Book: isbn=%s, title=%s, price=%.2f, available=%s" %(self.isbn, self.title, self.price, self.available)
    def __repr__(self):
        return self.info()
    
class BookException(BaseException):
    def __init__(self, cause):
        self.cause = cause
    def __repr__(self):
        return "BookException: cause=%s" %(self.cause)
    def __str__(self):
        return "BookException, cause='%s'" %(self.cause)
class RestClientBooksService:

    assemble = lambda s, dict : Book(dict['isbn'], dict['title'], dict['price'])

    def __init__(self, base_url, store_service):
        self.store_service = store_service
        self.base_url = base_url

    def create(self, title, price=0.0):
        if (title == None or len(title.strip()) == 0):
            raise BookException(f"invalid title {title}")
        if (price < 0):
            raise BookException(f"invalid price {price}")
        response = requests.post(f"{self.base_url}/{title}")
        if (response.status_code != 200):
            raise BookException(f"server error")

        isbn = response.text
        return isbn

    def find_all(self):
        response = requests.get(f"{self.base_url}")
        if (response.status_code != 200):
            raise BookException(f"server error")
        book_json_list = response.json()
        return [self.assemble(book_dict) for book_dict in book_json_list]

    def find_by_isbn(self, isbn):
        if (isbn == None or len(isbn.strip()) == 0):
            raise BookException(f"invalid isbn {isbn}")
        response = requests.get(f"{self.base_url}/{isbn}")
        if (response.status_code != 200):
            raise BookException(f"server error")
        book_dict = response.json()
        book = self.assemble(book_dict)
        if (book == None):
            raise BookException(f"book with isbn {isbn} not found")
        stock = self.store_service.get_stock("books", isbn)
        book.available = (stock > 0)
        return book

    def update(self, book):
        if (book == None or len(book.isbn.strip()) == 0):
            raise BookException(f"invalid isbn {book.isbn}")
        if (len(book.title.trim()) == 0):
            raise BookException(f"invalid title {book.title}")
        if (book.price < 0):
            raise BookException(f"invalid price {book.price}")
        if (book.pages <= 0):
            raise BookException(f"invalid pages {book.pages}")

        response = requests.put(f"{self.base_url}", book)
        if (response.status_code != 200):
            raise BookException(f"server error")

    def delete_by_isbn(self, isbn):
        if (isbn == None or len(isbn.strip()) == 0):
            raise BookException(f"invalid isbn {isbn}")
            response = requests.delete(f"{self.base_url}/{isbn}")
            if (response.status_code != 200):
                raise BookException(f"book with isbn {isbn} not found")
    
class BooksService:

    def __init__(self, store_service, isbngenerator):
        self.store_service = store_service
        self.isbngenerator = isbngenerator
        self.books = {}

    def create(self, title, price=0.0):
        if (title == None or len(title.strip()) == 0):
            raise BookException(f"invalid title {title}")
        if (price < 0):
            raise BookException(f"invalid price {price}")
        isbn = self.isbngenerator.next_isbn()
        book = Book(isbn, title, price)
        self.books[isbn] = book
        return isbn

    def find_all(self):
        return self.books.values()
    def find_by_isbn(self, isbn):
        if (isbn == None or len(isbn.strip()) == 0):
            raise BookException(f"invalid isbn {isbn}")
        book = self.books.get(isbn, None)
        if (book == None):
            raise BookException(f"book with isbn {isbn} not found")
        stock = self.store_service.get_stock("books", isbn)
        book.available = (stock > 0)
        return book

    def update(self, book):
        if (book == None or len(book.isbn.strip()) == 0):
            raise BookException(f"invalid isbn {book.isbn}")
        if (len(book.title.strip()) == 0):
            raise BookException(f"invalid title {book.title}")
        if (book.price < 0):
            raise BookException(f"invalid price {book.price}")
        book = self.books.get(book.isbn, None)
        if (book == None):
            raise BookException(f"book with isbn {book.isbn} not found")
        self.books[book.isbn] = book

    def delete_by_isbn(self, isbn):
        if (isbn == None or len(isbn.strip()) == 0):
            raise BookException(f"invalid isbn {isbn}")
        book = self.books.get(isbn, None)
        if (book == None):
            raise BookException(f"book with isbn {isbn} not found")
        else:
            self.books.pop(isbn)    
