from publishing import Book, Publisher, Author
def main():
    p = Publisher('Springer')
    b1 = Book('ISBN1', 'Python in Action', 19.99, 200, p)
    b2 = Book('ISBN2', 'Java', 29.99, 666, p)
    a1 = Author('Schreiber', 'Ling')
    a2 = Author('Lite', 'Rat')

    p.books.append(b1)
    p.books.append(b2)
    a1.books.append(b1)
    b1.authors.add(a1)
    a1.books.append(b2)
    b2.authors.add(a1)
    a2.books.append(b2)
    b2.authors.add(a2)
    print('done')

    
if __name__ == '__main__':
    main()