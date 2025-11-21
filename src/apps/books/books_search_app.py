from books_service import BooksService

def main():
    books_service = BooksService()
    isbn = input('Enter the ISBN to search for: ')
    print(books_service.search_by(isbn))

main()