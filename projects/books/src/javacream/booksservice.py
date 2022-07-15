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

