class Book(object):
    def __init__(self, isbn, title, pages, price):
        self.isbn = isbn
        self.title = title
        self.pages = pages
        self.price = price
    def info(self):
        return "Book: isbn=%s, title=%s, pages=%.0f, price=%.2f" %(self.isbn, self.title, self.pages, self.price)
    def __repr__(self):
        return self.info()
    
class BookException(BaseException):
    def __init__(self, cause):
        self.cause = cause
    def __repr__(self):
        return "BookException: cause=%s" %(self.cause)
    def __str__(self):
        return "BookException, cause='%s'" %(self.cause)
    
        
class BooksService(object):

    def __init__(self, store_service, isbngenerator):
        self.store_service = store_service
        self.isbngenerator = isbngenerator
        self.books = {}

    def create(self, title, price=0.0, pages=1):
        if (title == None or len(title.strip()) == 0):
            raise BookException(f"invalid title {title}")
        if (price < 0 or pages <= 0):
            raise BookException(f"invalid price {price} or pages {pages}")
        isbn = self.isbngenerator.next_isbn()
        book = Book(isbn, title, pages, price)
        self.books[isbn] = book
        return isbn

    def find_by_isbn(self, isbn):
        if (isbn == None or len(isbn.strip()) == 0):
            raise BookException(f"invalid isbn {isbn}")
        book = self.books.get(isbn, None)
        if (book == None):
            raise BookException(f"book with isbn {isbn} not found")
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