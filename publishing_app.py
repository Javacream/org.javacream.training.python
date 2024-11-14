import publishing_service
def main():
    p = publishing_service.create_publisher('Springer')
    b1 = publishing_service.create_book('ISBN1', 'Python in Action', 19.99, 200, p)
    b2 = publishing_service.create_book('ISBN2', 'Java', 29.99, 666, p)
    a1 = publishing_service.create_author('Schreiber', 'Ling')
    a2 = publishing_service.create_author('Lite', 'Rat')
    publishing_service.write(a1, b1)
    publishing_service.write(a1, b2)
    publishing_service.write(a2, b2)
    print(publishing_service.find_all_authors())
    print(publishing_service.find_all_books())
    print(publishing_service.find_all_publishers())
    print(publishing_service.find_all_books())
    print(publishing_service.find_book_by('ISBN1'))
    print(publishing_service.find_publisher_by('Springer'))
    print(publishing_service.find_authors_by_lastname('Schreiber'))
    print('done')

    
if __name__ == '__main__':
    main()