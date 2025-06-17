from books import BooksService

def main():
    books_service = BooksService()
    generated_isbn = books_service.create('Python')
    searched = books_service.find_by_isbn(generated_isbn)
    print(f'Das Buch mit der ISBN {generated_isbn} hat den Titel {searched.title}')
    generated_isbn = books_service.create('Java')
    searched = books_service.find_by_isbn(generated_isbn)
    print(f'Das Buch mit der ISBN {generated_isbn} hat den Titel {searched.title}')
    print(searched)
if __name__ == '__main__':
    main()