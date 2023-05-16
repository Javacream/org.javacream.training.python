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
        self.postalCode + self.city.__hash__() + self.street.__hash__()

class Simple:
    def __str__(self):
        return "Hugo"

def test():
    ad1 = Address("München", 81373, "Marienplatz")
    ad2 = Address("München", 81373, "Marienplatz")
    au1 = Author(1, "Sawitzki", "Rainer")
    au2 = Author(1, "Sawitzki", "Rainer")

    s1 = "Hello"
    s2 = "Hello"

    print(s1 == s2)

    print(ad1 is ad2) # Sind die Referenzen identisch
    print(ad1 == ad2) # Sind die Inhalte identisch

    print(au1 is au2) # Sind die Referenzen identisch
    print(au1 == au2) # Sind die Inhalte identisch

    print(s1)
    print(ad1)
    print(ad2)
    print(au1)


    si = Simple()
    print(si)
test()    

