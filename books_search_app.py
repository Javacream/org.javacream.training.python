import books_search

def main():
    isbn = input('Bitte eine ISBN-Nummer eingeben: ')
    book = books_search.search(isbn)
    if book == ():
        print(f'Kein Buch mit der ISBN {isbn} gefunden')
    else:
        print(book)        

main()