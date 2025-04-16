class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = set()

class School:
    def __init__(self):
        self.courses = dict()
        self.students = dict()
        self.counter = 1
    def add(self, student):
        student.id = self.counter
        self.counter += 1
        self.students[student.id] = student
    def remove(self, student):
        self.students.pop(student.id)
    def get_info(self, id):
        return self.students.get(id)
    def get_students_for_course(self, title):
        course: Course = self.courses.get(title)
        return course.students


class Course:
    def __init__(self, title):
        self.title = title
        self.students = set()