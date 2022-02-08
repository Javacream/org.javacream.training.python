class Person:
    def __init__(self, id, lastname, firstname):
        #Constructor
        #self: Referenz auf das eben erzeugte Objekt
        self.id = id
        self.lastname = lastname
        self.firstname = firstname


a_person = Person(42, "Meier", "Hugo")
print(a_person)
print(dir(a_person))
print(type(a_person))