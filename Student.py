class Student:
    id = ''
    gpa = ''
    first_name = ''
    last_name = ''


def print_student(student):
    print(student.first_name + ", " + student.last_name + ", " + str(student.id) + ", " + str(student.gpa))


def main():
    student_1 = Student()
    student_1.id = 12
    student_1.gpa = 2.58
    student_1.first_name = "Alex"
    student_1.last_name = "Hunter"
    student_2 = Student()
    student_2.id = 14
    student_2.gpa = 3.33
    student_2.first_name = "Steve"
    student_2.last_name = "Rogers"

    print_student(student_1)
    print_student(student_2)


main()
