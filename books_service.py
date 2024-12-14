from book import Book
from math import inf
books = dict()
initial_isbn = 0
MIN_PRICE = 0
MIN_PAGES = 0
actual_isbn = initial_isbn
def create(title, price = 0, pages = 200, available = True):
    global actual_isbn
    actual_isbn += 1
    if price < MIN_PRICE:
        raise Exception(f'invalid price, must be greater or equal 0, was {price}')
    if pages <= MIN_PAGES:
        raise Exception(f'invalid page count, must be greater than 0, was {pages}')
    books[actual_isbn] = Book(actual_isbn, title, price, pages, available)
    return actual_isbn 
def find_all():
    return list(books.values())    
def find_by_isbn(isbn):
    return books.get(isbn)
def find_by_title(subtitle):
    return [b for b in books.values() if b.title.count(subtitle) > 0]
def find_by_price_range(min_price = 0, max_price = inf):
    return [b for b in books.values() if (b.price  >= min_price) and (b.price <= max_price)]
def delete_by(isbn):
    result =  books.pop(isbn, None)
    return result is not None