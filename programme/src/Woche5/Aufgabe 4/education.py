class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.courses = set()

class School:
    def __init__(self):
        self.courses = list()
        self.students = dict()
    def add(self, student):
        pass
    def remove(self, student):
        pass
    def get_info(id):
        pass
    def get_students_for_course(title):
        pass


class Course:
    def __init__(self, title):
        self.title
        self.students = set()