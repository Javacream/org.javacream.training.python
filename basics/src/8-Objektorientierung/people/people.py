class Person:
    def __init__(self, id, lastname, firstname):
        #Constructor
        #self: Referenz auf das eben erzeugte Objekt
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
    def say_hello(self):
        template = "my name is {} {}"
        return template.format(self.firstname, self.lastname)
    def __str__(self):
        elements = []
        for key, value in self.__dict__.items():
            elements.append('{key}={value}'.format(key=key, value=value))
        return ', '.join(elements)

class Address:
    def __init__(self, city, street):
        self.street = street
        self.city = city
    def __str__(self):
        return 'Address: city=' + self.city + ", street=" + self.street