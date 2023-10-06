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

    
class __PeopleManager__:
    __counter__ = -1
    __default_height__ = 167
    def __init__(self):
        self.__people__ = {}
    
    def create(self, lastname, firstname):
        __PeopleManager__.__counter__ += 1
        new_person = Person(lastname, firstname, __PeopleManager__.__default_height__)
        self.__people__[__PeopleManager__.__counter__] = new_person
        return __PeopleManager__.__counter__

    def find_by_id(self, id):
        return self.__people__.get(id) # get retrives None if key not present, [id] would raise an exception

    def delete_by_id(self, id):
        deleted = self.__people__.pop(id, None)
        return deleted != None

name = 'people'
people_manager = __PeopleManager__()
if __name__ == "__main__":
    print("################ people  module " + __name__)