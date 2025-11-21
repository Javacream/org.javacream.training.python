from books_service import search_by
def main():
    isbn = input('Enter the ISBN to search for: ')
    print(search_by(isbn))

main()