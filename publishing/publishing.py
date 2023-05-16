class Publisher:
    def __init__(self, name, address):
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
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
        self.books = {}

class Address:
    def __init__(self, city, postalCode, street):
        self.city = city
        self.street = street
        self.postalCode = postalCode


def test():
    def testPublisherOk():
        p = Publisher("Springer", Address("Berlin", 30111, "Alexanderplatz"))
    def testPublisherWrong():
        try:
            p = Publisher("Springer")
            print("CREATING PUBLISHER WITH ONE PARAM MUST FAIL")
        except:
            pass    
    def testBookOk():
        b = Book("ISBN1", "Title1", 200, 19.99, True)
    def testAuthorOk():
        a = Author("Schneider", "Hannah")
    def testAddressOk():
        a = Address("Berlin", 30111, "Alexanderplatz")

    print("Starting  all tests: Done")
    testPublisherOk()
    testPublisherWrong()
    testBookOk()
    testAddressOk()
    testAuthorOk()
    print("Running  all tests: Done")
test()