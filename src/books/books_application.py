import argparse
import sys

sys.path.append('/home/rainersawitzki/git/org.javacream.training.python/src')

from books.application_context_remote import books_service

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="books script")
    parser.add_argument('--env', choices=['local', 'remote'], help="name of environment", type=str, required=True )
    #parser.add_argument('--hugo', help="just for fun", type=str)
    args= vars(parser.parse_args())
    env = args['env']
    if (env == 'local'):
        from books.application_context_local import books_service
    else:
        from books.application_context_remote import books_service

    # book = books_service.create("Python")
    # books_service.create("Java")
    # books_service.create("PHP")
    print(books_service.find_all())

