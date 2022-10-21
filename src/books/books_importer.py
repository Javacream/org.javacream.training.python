import json
import os
import sys

sys.path.append('/home/rainersawitzki/git/org.javacream.training.python/src')

from books.application_context import books_service
from books.booksservice import Book

if __name__=='__main__':
    script_dir = os.path.dirname(os.path.realpath(__file__))
    data_file = script_dir + '/books_input.json'

    
    with open(data_file) as f:
        json_books = json.load(f)
        for json_book in json_books:
            book = Book(json_book['isbn'], json_book['title'], json_book['price'])
            books_service.books[book.isbn] = book
    print(books_service.find_all())
            

