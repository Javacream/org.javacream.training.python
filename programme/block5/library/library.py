import sys
sys.path.append('./programme/block5')
from people.people import Person

class Book:
    def __init__(self, title:str, author: Person, genre:str, status = False):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
class Library:
    def __init__(self):
        self.books: set[Book] = set()

    def append(self, book: Book):
        self.books.add(book)
    
    def lend(self, book: Book):
        if book.status:
            raise Exception(f'Book {book.title} is already lended')
        book.status = True

    def show(self):
        result = []
        for book in self.books:
            if book.status == False:
                result.append(book)
        return result