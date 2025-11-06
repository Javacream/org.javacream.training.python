from education import *
def main():
    s1 = Student('Einstein', 81)
    s2 = Student('Musterperson', 21)
    school = School()
    print(school.get_student_ids())
    id1 = school.add(s1)
    id2 = school.add(s2)

    print(school.get_student_ids())

    school.enroll(id1, "Python Programming")
    school.enroll(id2, "Python Programming")
    school.enroll(id2, "AI")
    school.enroll(id2, "Cooking")
    school.enroll(42, "AI")

    print(school.get_info(id1))

    for student in school.get_students_for_course("Python Programming"):
        print(student.name)
    print(school.get_info(42))


main()