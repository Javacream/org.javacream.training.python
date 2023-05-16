class Publisher:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        self.books = set()

class Book:
    def __init__(self, isbn, title, pages, price, available):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.pages = pages
        self.available = available
        self.authors = []

class Author:
    def __init__(self, id, lastname, firstname):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.books = set()

class Address:
    def __init__(self, city, postalCode, street):
        self.city = city
        self.street = street
        self.postalCode = postalCode
    def __str__(self):
        return f"Address: {self.street} {self.postalCode} {self.city}"
    def __eq__(self, other):
        return self.city == other.city and self.street == other.street and self.postalCode == other.postalCode
    def __hash__(self): #__eq__ und __hash__ sind die Grundlage des keys eines Dictionaries: falls __eq__ true liefert muss der Hash identisch sein
        return self.postalCode + self.city.__hash__() + self.street.__hash__()

class PublisherController:
    def __init__(self):
        self.__publishers = {}
        self.__counter = 0
    def create(self, name, address):
        newPublisher =  Publisher(self.__counter, name, address)
        self.__publishers[newPublisher.id] = newPublisher
        self.__counter = self.__counter + 1
        return newPublisher.id
    def findById(self, publisherId):
        return self.__publishers.get(publisherId)

class AuthorController:
    def __init__(self):
        self.__authors = {}
        self.__counter = 0
    def create(self, lastname, firstname):
        newAuthor =  Author(self.__counter, lastname, firstname)
        self.__authors[newAuthor.id] = newAuthor
        self.__counter = self.__counter + 1
        return newAuthor.id
    def findById(self, authorId):
        return self.__authors.get(authorId)

class BookController:
    def __init__(self):
        self.__books = {}
    def create(self, isbn, title, pages, price, available):
        newBook =  Book(isbn, title, pages, price, available)
        self.__books[newBook.isbn] = newBook
        return newBook.isbn
    def findById(self, isbn):
        return self.__books.get(isbn)


def test():
    publisher = Publisher(1, "Springer", Address("Berlin", 30333, "Alexanderplatz"))
    book1 = Book("ISBN1", "Python Programming", 500, 9.99, True)
    book2 = Book("ISBN2", "Monty Python", 200, 19.99, False)
    book3 = Book("ISBN3", "Java Programming", 50, 29.99, True)
    book4 = Book("ISBN4", "Python Advanced", 900, 5.99, True)
    book5 = Book("ISBN5", "Web Programming Java", 700, 49.99, False)
    publisher.books.add(book1)
    publisher.books.add(book2)
    publisher.books.add(book3)
    publisher.books.add(book4)
    publisher.books.add(book5)
    [print(b.title) for b in publisher.books if b.price > 25] 
    [print(b.title) for b in publisher.books if b.pages > 500] 
    [print(b.title) for b in publisher.books if b.title.count("Python") > 0] 
    [print(b.title) for b in publisher.books if b.price < 15 and b.available] 

test()
