from publishing.booksservice import BooksService
from publishing.context import context
from publishing.utilities import IllegalParameterException


if __name__ == '__main__':
    bs = context().bookservice
    bs = BooksService()
    try:
        isbn = bs.new("Demo", 200, 19.99)
    except IllegalParameterException:
        pass
    print "Generated isbn: " + isbn
    books = bs.find_all()
    print(books)
    book = bs.find_book_by_isbn(isbn);
    print book.info()
    bs.update(isbn, pages=300, price= 29.99)
    book = bs.find_book_by_isbn(isbn);
    print book.info()
    bs.delete_book_by_isbn(isbn)
    books = bs.find_all()
    print books
    bs.update("Hugo", pages=300, price= 29.99)
    print bs.find_all()
    