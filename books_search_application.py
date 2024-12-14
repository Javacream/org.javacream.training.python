import books_service

def main():
    books_service.load()
    while True:
        user_input = input("Please enter a search isbn (integer) or 'exit' to finish: ")
        if user_input == 'exit':
            break
        try:
            isbn = int(user_input)
            book = books_service.find_by_isbn(isbn)
            if book == None:
                print(f'searching for isbn {isbn} did not find a book')
            else:
                print(f'searching for isbn {isbn} found book {book}')    
        except:
            print(f'isbn must be an integer, you entered {user_input}')    
if __name__ == '__main__':
    main()