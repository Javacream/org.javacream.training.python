import os
import pickle
import sys

sys.path.append('/home/rainersawitzki/git/org.javacream.training.python/src')

from books.application_context import books_service

if __name__=='__main__':
    book = books_service.create("Python")
    print(book)
    books_service.create("Java")
    books_service.create("PHP")

    script_dir = os.path.dirname(os.path.realpath(__file__))
    data_file = script_dir + '/books_output.pickle'

    with open(data_file, 'wb') as f:
        pickle.dump(books_service.books, f)
    

