from publishing_types import Publisher, Book, Author
import os
import json
import datetime
class PublishingService:
    DATA_FILE = 'src/15/publishing.json'
    DATE_FORMAT = '%m/%d/%Y, %H:%M:%S'
    def __init__(self):
        self.publishers = dict()
        self.books = dict()
        self.authors = dict()
        self.publishers_counter = 0
        self.books_counter = 0
        self.authors_counter = 0
    def load(self):
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, encoding='utf-8') as file:
                data = json.load(file)
                for raw_publisher_entry in data:
                    raw_publisher = raw_publisher_entry['publisher']
                    publisher = Publisher(int(raw_publisher['id']), raw_publisher['name'])
                    self.publishers[publisher.id] = publisher
                    raw_books = raw_publisher['books']
                    for raw_book in raw_books:
                        book = Book(raw_book['isbn'], raw_book['title'], float(raw_book['price']), int(raw_book['pages']), publisher)
                        self.books[book.isbn] = book
                        book.publishing_date = datetime.datetime.strptime(raw_book['publishing_date'], self.DATE_FORMAT)
                        publisher.books.add(book)
                        for raw_author in raw_book['authors']:
                            author = Author(int(raw_author['id']), raw_author['lastname'], raw_author['firstname'])
                            self.authors[author.id] = author
                            book.authors.append(author)
                            author.books.append(book)
                    self.publishers_counter = max(self.publishers.keys()) + 1
                    self.books_counter = len(self.books)
                    self.authors_counter = max(self.authors.keys()) + 1
    def save(self):
        with open(self.DATA_FILE, 'wt', encoding='utf-8') as file:
            json.dump(self.serialize(self.publishers), file)
    def serialize(self, publishers):
        return [
                {
                'id': publisher.id,
                'publisher':{ 
                    'id': publisher.id,
                    'name': publisher.name,
                    'books': [
                        {
                            'isbn': book.isbn,
                            'title': book.title,
                            'price': book.price,
                            'pages': book.pages,
                            'publishing_date': book.publishing_date.strftime(self.DATE_FORMAT),
                            'authors': [
                                {
                                    'id': author.id,
                                    'lastname': author.lastname,
                                    'firstname': author.firstname
                                }for author in book.authors
                            ]
                        } for book in publisher.books
                    ]
                }
            }
            for publisher in publishers.values()
        ]        
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

    def books_more_expensive_than(self, min_price):
        return [book for book in self.books.values() if book.price > min_price]
    def authors_for_publisher(self, publisher):
        return {author for book in publisher.books for author in book.authors}
    def authors_for_publisher_with_lastname(self, publisher, lastname):
        return {author for book in publisher.books for author in book.authors if author.lastname == lastname}
