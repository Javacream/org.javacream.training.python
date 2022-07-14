class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Person:
    def __init__(self, lastname, firstname, height, gender):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.gender = gender

    def say_hello(self):
        return f"Hello, my name is {self.firstname} {self.lastname}"

    def set_address(self, address):
        self.address = address

    def marry(self, partner):
        if hasattr(self, 'partner'):
            print("cannot marry again")
            return False
        if hasattr(partner, 'partner'):
            print("cannot marry, partner is married")
            return False
        if partner == self:
            print("cannot marry myself")
            return False
        self.partner = partner
        partner.partner = self    
        return True

    def divorce(self):
        if (not hasattr(self, 'partner')):
            print("cannot be divorced, not married")
            return False
        delattr(self.partner, 'partner')
        delattr(self, 'partner')
        return True

person1 = Person("Sawitzki", "Rainer", 183, 'm')
person2 = Person("Meier", "Hannah", 199, 'f')
person3 = Person("Mustermann", "Hans", 139, 'd')
address1 = Address("München", "Marienplatz")
address2 = Address("Berlin", "Alexanderplatz")

person1.set_address(address1)
person1.set_address(address2)

print(person1.say_hello())
print(f"person1 marries person2: {person1.marry(person2)}")
print(f"person3 marries person2: {person3.marry(person2)}")
print(f"person2 marries person3: {person2.marry(person3)}")
print(f"person3 marries person3: {person3.marry(person3)}")
print(f"person3 divorce: {person3.divorce()}")
print(f"person2 divorce: {person2.divorce()}")
print(f"person3 marries person2: {person3.marry(person2)}")


