import argparse
import re
import sys

sys.path.append('/home/rainersawitzki/git/org.javacream.training.python/src')

from books.application_context import books_service

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="books script")
    parser.add_argument('--env', choices=['local', 'remote'], help="name of environment", type=str, nargs=1, required=True )
    parser.add_argument('--hugo', help="just for fun", type=str)
    args= parser.parse_args()
    print(args)
    book = books_service.create("Python")
    print(book)
    books_service.create("Java")
    books_service.create("PHP")
    print(books_service.find_all())

