from javacream.context import context

if __name__ == '__main__':
    bs = context.books_service
    isbn = bs.create("Demo", 200, 19.99)
    print ("Generated isbn: " + isbn)
    book = bs.find_by_isbn(isbn)
    print (book.info())
    bs.delete_by_isbn(isbn)
