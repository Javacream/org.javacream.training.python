import sys

sys.path.append('/home/rainersawitzki/git/org.javacream.training.python/src')

from books.application_context import books_service

if __name__=='__main__':
    book = books_service.create("Python")
    print(book)
    books_service.create("Java")
    books_service.create("PHP")
    print(books_service.find_all())

