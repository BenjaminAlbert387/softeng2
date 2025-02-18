
student_check = input("Please enter the name of the student you want to find: ")

with open('assignment2file.txt') as f:
    if student_check in f.read():
        print('Yes, student is there')

        class Person:
            def __init__(self, name):
                self.name = name
                #self.identifier = identifier

        p1 = Person(student_check)

        print(p1.name)

    else:
        print('No, invalid')