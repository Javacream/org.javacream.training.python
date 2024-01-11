from _pyio import open
import pickle

from publishing.utilities import checkNoneOrEmptyParameter, \
    IllegalParameterException


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
    def __init__(self):
        #self.books = {}
        self.books = self.load();
    def init(self, isbngenerator = None, storeservice = None):
        self.isbngenerator = isbngenerator
        self.storeservice = storeservice
    
    def new(self, title, pages=1, price=0):
        checkNoneOrEmptyParameter(title, "title")
        if pages <= 0:
            raise IllegalParameterException("Illegal pages: "+ str(pages))
        if price < 0:
            raise IllegalParameterException("Illegal price: "+ str(price))
        isbn = self.isbngenerator.next_isbn()
        print ("generated isbn %s" %(isbn))
        book = Book(self.isbngenerator.next_isbn(), title, pages, price)
        self.books[book.isbn] = book
        self.save()
        return book.isbn
    def find_book_by_isbn(self, isbn):
        checkNoneOrEmptyParameter(isbn, "isbn")
        if not isbn in self.books:
            raise BookException("Book with isbn %s not found" %(isbn))
        book = self.books[isbn]
        stock = self.storeservice.get_stock("books", book.isbn)
        # print "Retrieved stock is %.0f" % (stock)
        book.available = (stock >= 0)
        return book
    def delete_book_by_isbn(self, isbn):
        checkNoneOrEmptyParameter(isbn, "isbn")
        self.books.pop(isbn)            
        self.save()
    def find_all(self):
        return self.books.values()
    def update(self, isbn, **values):
        checkNoneOrEmptyParameter(isbn, "isbn")
        price = values.get("price", None)
        pages = values.get("pages", None)
        if isbn in self.books:
            book = self.books[isbn]
        else:
            raise BookException("Book with isbn %s not found for update" %(isbn))
        if price: 
            if price >= 0:
                book.price = price
            else:
                raise BookException("Illegal price %.2f" %(price))    
        if pages:
            if pages > 0:
                book.pages = pages
            else:
                raise BookException("Illegal pages %.0f"%(pages))    
        self.save()

        
    def save(self):
        pickleFile = open("books.pkl", "wb")
        pickle.dump(self.books, pickleFile, protocol=-1)
    def load(self):
        try:
            pickleFile = open("books.pkl", "rb")
            return pickle.load(pickleFile)
        except IOError:
            return {}