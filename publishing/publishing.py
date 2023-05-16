class Publisher:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        self.books = {}

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
        self.books = {}

class Address:
    def __init__(self, city, postalCode, street):
        self.city = city
        self.street = street
        self.postalCode = postalCode

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
    def testPublisherOk():
        p = Publisher(1, "Springer", Address("Berlin", 30111, "Alexanderplatz"))
    def testPublisherWrong():
        try:
            p = Publisher("Springer")
            print("CREATING PUBLISHER WITH ONE PARAM MUST FAIL")
        except:
            pass    
    def testBookOk():
        b = Book("ISBN1", "Title1", 200, 19.99, True)
    def testAuthorOk():
        a = Author(1, "Schneider", "Hannah")
    def testAddressOk():
        a = Address("Berlin", 30111, "Alexanderplatz")
    def testPublisherController():
        controller = PublisherController()
        createdId = controller.create("Springer", Address("Berlin", 30111, "Alexanderplatz"))
        print(f"createdId={createdId}")
        publisher = controller.findById(createdId)
        print(f"found publisher, name={publisher.name}")
        createdId = controller.create("Addison", Address("Berlin", 30111, "Alexanderplatz"))
        print(f"createdId={createdId}")
        publisher = controller.findById(createdId)
        print(f"found publisher, name={publisher.name}")

    def testAuthorController():
        authorController = AuthorController()
        id = authorController.create("Meier", "Hans")
        print(f"created author id={id}")
        author = authorController.findById(id)
        print(f"found author, lastname={author.lastname}")
    def testBookController():
        bookController = BookController()
        isbn = bookController.create("ISBN1", "Title1", 200, 19.99, True)
        print(f"created book isbn={isbn}")
        book = bookController.findById(isbn)
        print(f"found book, lastname={book.title}")

    print("Starting  all tests...")
    testPublisherOk()
    testPublisherWrong()
    testBookOk()
    testAddressOk()
    testAuthorOk()
    testPublisherController()
    testAuthorController()
    testBookController()
    print("Running  all tests: Done")
test()