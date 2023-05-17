import unittest
import json

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
    def __str__(self):
        return f"Author: lastname={self.lastname}, firstname={self.firstname}"

class AddressController:
    def __init__(self):
        self.addresses = []
        with open ('./publishing/addresses.json') as file:
            [self.addresses.append(Address(jsonAddress["city"], jsonAddress["postalCode"], jsonAddress["street"])) for jsonAddress in json.load(file)]

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
        self.__readAuthorsFromFile()
    def __create(self, lastname, firstname):
        newAuthor =  Author(self.__counter, lastname, firstname)
        self.__authors[newAuthor.id] = newAuthor
        self.__counter = self.__counter + 1
    def create(self, lastname, firstname):
        newAuthor =  Author(self.__counter, lastname, firstname)
        self.__authors[newAuthor.id] = newAuthor
        self.__counter = self.__counter + 1
        try:
            with open('./publishing/authors.txt', 'a') as authorsFile:
                authorsFile.write(f"\n{lastname},{firstname}")
        except Exception as e:
            print(e)
        return newAuthor.id

    def findById(self, authorId):
        return self.__authors.get(authorId)
    def __readAuthorsFromFile(self):
        try:
            with open ('./publishing/authors.txt', 'r') as authorsFile:
                [self.__create(*line.split(",")) for line in authorsFile]#*: Verwandelt eine Liste in eine Folge von Parametern
        except Exception as e:
            print(e)
            
class BookController:
    def __init__(self):
        self.__books = {}
    def create(self, isbn, title, pages, price, available):
        newBook =  Book(isbn, title, pages, price, available)
        self.__books[newBook.isbn] = newBook
        return newBook.isbn
    def findById(self, isbn):
        return self.__books.get(isbn)

class AuthorControllerTest(unittest.TestCase):
    def testLoadData(self):
        ac = AuthorController()
        expectedLastname = "Lastname"
        result = ac.findById(1)
        self.assertEqual(expectedLastname, result.lastname)
class AddressControllerTest(unittest.TestCase):
    def testLoadData(self):
        ac = AddressController()
        self.assertEqual(3, len(ac.addresses))
        self.assertEqual("Münchens", ac.addresses[0].city)


if __name__ == '__main__':
    unittest.main()
