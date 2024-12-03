class Student:
    def __init__(self, id, name, age, course):
        self.id = id
        self.name = name
        self.age = age
        self.course = course

class School:
    def __init__(self):
        self.students = dict()
    def add(self, student):
        self.students.update(student.id, student)
    def remove(self, student):
        self.students.pop(student.id, student)
    def get(self, id):
        return self.students.pop(id)
    
    def get_student_for_course(self, course):
        return [s for s in self.students.values() if s.course == course]