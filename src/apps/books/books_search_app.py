from books_service import BooksService

def main():
    books_service = BooksService()
    user_input = input('Enter the ISBN to search for or a for all books: ')
    if user_input == 'a':
        print(books_service.find_all())
    else:
        isbn = user_input
        print(books_service.search_by(isbn))

main()