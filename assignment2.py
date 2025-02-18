student_file = open("assignment2file.txt", "r")


class Student:
    def __init__(student, name, identifier):
        student.name = name
        student.identifier = identifier

p1 = Student("Alice", 1001)

print(p1.name)
print(student_file.readlines())