class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = set()
class School:
    def __init__(self):
        self.courses = dict()
        self.students = dict()
        self.student_counter = 1
        self.init_courses()

    def add(self, student):
        student.id = self.student_counter
        self.student_counter += 1
        self.students[student.id] = student
        return student.id

    def init_courses(self):
        self.add_course("Python Programming")
        self.add_course("AI")

    def add_course(self, title):
        course = Course(title)
        self.courses[title] = course

    def get_courses(self):
        return list(self.courses.values())
    
    def remove(self, id):
        removed_student = self.students.pop(id)
        return removed_student

    def get_student_ids(self):
        return list(self.students.keys())
    
    def enroll(self, id, title):
        student:Student = self.students.get(id)
        if not student:
            print(f"cannot enroll, unknown student id: {id} ")
            return False
        course:Course = self.courses.get(title);
        if not course:
            print(f"cannot enroll, unknown course title: {title} ")
            return False
        student.courses.add(course)
        course.students.add(student)

    def get_info(self, id):
        return self.students.get(id)
    
    def get_students_for_course(self, title):
        course: Course = self.courses.get(title)
        if not course:
            return set()
        else:
            return course.students
class Course:
    def __init__(self, title):
        self.title = title
        self.students = set()