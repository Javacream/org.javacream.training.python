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
    __counter__ = -1
    __default_height__ = 167
    def __init__(self):
        self.__people__ = {}
    
    def create(self, lastname, firstname):
        PeopleManager.__counter__ += 1
        new_person = Person(lastname, firstname, PeopleManager.__default_height__)
        self.__people__[PeopleManager.__counter__] = new_person
        return PeopleManager.__counter__

    def find_by_id(self, id):
        return self.__people__.get(id) # get retrives None if key not present, [id] would raise an exception

    def delete_by_id(self, id):
        deleted = self.__people__.pop(id, None)
        return deleted != None

def main():

    people_manager = PeopleManager()
    people_manager.create("Goo", "Georg")
    people_manager.create("Foo", "Henry")

    search_result = people_manager.find_by_id(0)
    print(search_result.info())
    print(people_manager.delete_by_id(0))
    print(people_manager.delete_by_id(0))

main()