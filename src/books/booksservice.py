class Book(object):
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

