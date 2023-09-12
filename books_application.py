# creates a cleaned books file without duplicated isbns and a file containing isbn duplicated
import books

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
    with open('books_cleaned.csv', 'w') as cleaned_file:
        for isbn in books_by_isbn:
            if len(books_by_isbn[isbn]) == 1:
                cleaned_file.write(books_by_isbn[isbn][0])
            else:
                duplicate_isbns.add(isbn)
    # write the duplicates file
    with open('duplicate_isbns.csv', 'w') as duplicates:
        for isbn in duplicate_isbns:
            duplicates.write(isbn + '\n')

def write_python_books(manager):
    result_list = manager.books_with_title_containing_python()
    filename = 'python_books.txt'
    with open (filename, 'w') as file:
        file.writelines([b.__str__() + '\n' for b in result_list])
def write_expensive_books(manager):
    result_list = manager.books_with_price_greater_than_50()
    filename = 'expensive_books.txt'
    with open (filename, 'w') as file:
        file.writelines([b.__str__() + '\n' for b in result_list])
def write_average_price(manager):
    result = manager.average_book_price()
    filename = 'average_book_price.txt'
    with open (filename, 'w') as file:
        file.write(str(result))

def write_shortes_and_longest_title(manager):
    result = manager.books_with_shortest_and_longest_title()
    min_title_result_list = result[0]
    max_title_result_list = result[1]
    filename = 'min_max_txt'
    with open (filename, 'w') as file:
        file.write('Books with shortest title:\n')
        file.writelines([b.__str__() + '\n' for b in min_title_result_list])
        file.write('Books with longest title:\n')
        file.writelines([b.__str__() + '\n' for b in max_title_result_list])

def load_books():
    filename = 'books_cleaned.csv'
    with open(filename, 'r') as file:
        books_dict = dict()
        title_row = True
        for row in file:
            if (title_row):
                title_row = False
                continue
            data = row.split(',')
            isbn = data[0]
            title = data[1]
            price_str = data[2]
            # remove \n
            price_str = price_str[0: len(price_str) - 1]
            
            price = float(price_str)
            new_book = books.Book(isbn, title, price)
            books_dict[isbn] = new_book
            
    return books_dict
def analyse():
    books_dict = load_books()
    books_manager = books.BooksManager(books_dict)
    write_python_books(books_manager)
    write_expensive_books(books_manager)
    write_average_price(books_manager)
    write_shortes_and_longest_title(books_manager)

def main():
    cleanup()
    analyse()
main()