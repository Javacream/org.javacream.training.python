import books

def main():
    isbn = input('Bitte eine ISBN-Nummer eingeben: ')
    book = books.search(isbn)
    if book == ():
        print(f'Kein Buch mit der ISBN {isbn} gefunden')
    else:
        print(book)        

main()