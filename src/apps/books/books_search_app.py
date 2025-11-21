from books_service import BooksService

def main():
    books_service = BooksService()
    user_input = input('Enter the ISBN to search for or a for all books: ')
    if user_input == 'a':
        books = books_service.find_all()
        print(books)
    else:
        isbn = user_input
        book = books_service.search_by(isbn) 
        print(book.title)

main()