import os 
dir_path = os.path.dirname(os.path.realpath(__file__))


import sys
sys.path.append(dir_path + '/..')

from javacream.booksservice import BookException
from javacream.context import context
from javacream.utilities import IllegalParameterException


if __name__ == '__main__':
    bs = context().bookservice
    try:
        isbn = bs.new("Demo", 200, 19.99)
    except IllegalParameterException:
        pass
    print ("Generated isbn: " + isbn)
    books = bs.find_all()
    print(books)
    book = bs.find_book_by_isbn(isbn)
    print (book.info())
    bs.update(isbn, pages=300, price= 29.99)
    book = bs.find_book_by_isbn(isbn)
    print (book.info())
    bs.delete_book_by_isbn(isbn)
    books = bs.find_all()
    print (books)
    try:
        bs.update(isbn, pages=300, price= 29.99)
    except BookException:
        pass
    