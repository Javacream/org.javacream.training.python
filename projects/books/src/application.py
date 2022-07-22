import argparse
from javacream.booksservice import Book
from javacream.context import context

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="books script")
    parser.add_argument('env', choices=['local', 'remote'], metavar="Environment", type=str, nargs=1, help="name of environment")
    parser.parse_args()

    #Idee
    #Migrationsskript: 
    # Bücher aus dem WebService lesen, availability ist aber immer 'false'
    # Pro Buch ein get_stock im StoreService
    # Ausgabe der Bücher mit der tatsächlichen Availability 


    

