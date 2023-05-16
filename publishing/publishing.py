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
    def __init__(self, lastname, firstname):
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
        a = Author("Schneider", "Hannah")
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

    print("Starting  all tests...")
    testPublisherOk()
    testPublisherWrong()
    testBookOk()
    testAddressOk()
    testAuthorOk()
    testPublisherController()
    print("Running  all tests: Done")
test()