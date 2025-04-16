from education import *
def main():
    s1 = Student('Einstein', 81)
    s2 = Student('Musterperson', 21)
    school = School()
    c1 = Course('Python Programming')
    c2 = Course('AI')

    school.courses[c1.title] = c1
    school.courses[c2.title] = c2
    school.add(s1)
    school.add(s2)

    s1.courses.add(c1)
    c1.students.add(s1)
    s1.courses.add(c2)
    c2.students.add(s1)
    
    s2.courses.add(c1)
    c1.students.add(s2)

    print(school.get_info(1))
    print(school.get_students_for_course("Python Programming"))


main()