

class Person:
    # a static attribute, part of the class object
    info_template = "Hello, my name is {} {}"

    # constructor
    def __init__(self, lastname, firstname, height):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height

    def info(self):
        return Person.info_template.format(self.firstname, self.lastname)

class PeopleManager:
    def __init__(self):
        self.__people__ = {}
    
    def create(self, lastname, firstname):
        default_height = 167
        counter = 0
        new_person = Person(lastname, firstname, default_height)
        self.__people__[counter] = new_person
        counter = counter + 1
        return counter

    def find_by_id(self, id):
        return self.__people__[id]

    def delete_by_id(self, id):
        self.__people__.pop(id)
        return True

def main():

    people_manager = PeopleManager()
    people_manager.create("Goo", "Georg")
    people_manager.create("Foo", "Henry")

    search_result = people_manager.find_by_id(0)
    print(search_result.info())

main()