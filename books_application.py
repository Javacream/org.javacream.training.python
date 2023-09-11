# creates a cleaned books file without duplicated isbns and a file containing isbn duplicated
def cleanup():
    books_by_isbn = dict()
    # read all lines to a dict using isbn as key and a list of rows
    with open('books.csv', 'r') as file:
        for row in file:
            isbn = row.split(',')[0]
            if not isbn in books_by_isbn:
                isbn_rows = []
                books_by_isbn[isbn] = isbn_rows
                isbn_rows.append(row)
            else:
                books_by_isbn[isbn].append(row)    
    duplicate_isbns = set()
    # check if the row length of a given isbn is 1. if not, the isbn is duplicated and the row is therefor dismissed
    with open('book_cleaned.csv', 'w') as cleaned_file:
        for isbn in books_by_isbn:
            if len(books_by_isbn[isbn]) == 1:
                cleaned_file.write(books_by_isbn[isbn][0])
            else:
                duplicate_isbns.add(isbn)
    # write the duplicates file
    with open('duplicate_isbns.csv', 'w') as duplicates:
        for isbn in duplicate_isbns:
            duplicates.write(isbn + '\n')
def main():
    cleanup()

main()