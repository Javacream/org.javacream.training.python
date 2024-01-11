class Publisher:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = set()
    def __repr__(self):
        return f'Publisher(id={self.id}, name={self.name})'
    def __eq__(self, other):
        if isinstance(other, Publisher):
            return self.id == other.id
        else:
            return False
    def __hash__(self):
        return hash(self.id)

class Book:
    def __init__(self, isbn, title, price, pages, publisher):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.pages = pages
        self.publisher = publisher
        self.authors = []
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        else:
            return False
    def __hash__(self):
        return hash(self.isbn)
    def __repr__(self):
        return f'Book(isbn={self.isbn}, title={self.title}, price={self.price}, pages={self.pages}, publisher={self.publisher})'

class Author:
    def __init__(self, id, lastname, firstname):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.books = []
    def __repr__(self):
        return f'Author(id={self.id}, lastname={self.lastname}, firstname={self.firstname})'
class PublishingService:
    def __init__(self):
        self.publishers = dict()
        self.books = dict()
        self.authors = dict()
        self.publishers_counter = 0
        self.books_counter = 0
        self.authors_counter = 0
    def new_publisher(self, name):
        self.publishers_counter += 1
        new_publisher = Publisher(self.publishers_counter, name)
        self.publishers[new_publisher.id] = new_publisher
        return new_publisher

    def new_book(self, title, price, pages, publisher: Publisher):
        self.books_counter += 1
        new_book = Book(f'ISBN-{self.books_counter}', title, price, pages, publisher)
        self.books[new_book.isbn] = new_book
        publisher.books.add(new_book)
        return new_book
    def new_author(self, lastname, firstname): 
        self.authors_counter += 1
        new_author = Author(self.authors_counter, lastname, firstname)
        self.authors[new_author.id] = new_author
        return new_author
    def written_by(self, book:Book, author:Author):
        book.authors.append(author)
        author.books.append(book)

def main():
    publishing_service = PublishingService()
    publisher1 = publishing_service.new_publisher('Springer')
    publisher2 = publishing_service.new_publisher('Addison')
    book1 = publishing_service.new_book('Java', 19.99, 200, publisher1)
    book2 = publishing_service.new_book('Spring', 29.99, 500, publisher1)
    book3 = publishing_service.new_book('Python', 15.55, 300, publisher2)
    author1 = publishing_service.new_author('Schneider', 'Hannah')
    author2 = publishing_service.new_author('Meier', 'Hans')
    publishing_service.written_by(book1, author1)
    publishing_service.written_by(book1, author2)
    publishing_service.written_by(book2, author2)
    publishing_service.written_by(book3, author1)
    print('done')

main() 
