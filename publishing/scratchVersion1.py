class Address:
    def __init__(self, city, postalCode, street):
        self.city = city
        self.street = street
        self.postalCode = postalCode
    # def __str__(self):
    #     return f"Address: {self.street} {self.postalCode} {self.city}"
    # def __eq__(self, other):
    #     return self.city == other.city and self.street == other.street and self.postalCode == other.postalCode
    # def __hash__(self): #__eq__ und __hash__ sind die Grundlage des keys eines Dictionaries: falls __eq__ true liefert muss der Hash identisch sein
    #     self.postalCode + self.city.__hash__() + self.street.__hash__()

def test():
    ad1 = Address("München", 81373, "Marienplatz")
    ad2 = Address("München", 81373, "Marienplatz")
    ad3 = Address("Berlin", 30333, "Alexanderplatz")

    s = set()
    s.add(ad1)
    s.add(ad2)
    s.add(ad3)

    print(len(s))

    dict = {}
    dict[ad1] = "Hugo"
    print(dict.get(ad2))
test()    

