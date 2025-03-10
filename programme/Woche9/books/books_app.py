from books_service import BooksService
def main():
    books_service = BooksService()
    books = books_service.read_all()
    print(books)
    print(f'min price: {books_service.min_price(books)}')
    print(f'max price: {books_service.max_price(books)}')
    print(f'average price: {books_service.avg_price(books)}')
    books_service.update_price('ISBN1', 7.77)
    isbn = books_service.create("Python and REST")
    print(f'created new book with isbn {isbn}')
    print(books_service.find_by_isbn(isbn))
    books_service.delete_by_isbn(isbn)
    books_service.delete_by_isbn(isbn)
if __name__ == '__main__':
    main()