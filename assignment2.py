#*student_check = input("Please enter the name of the student you want to find: ")

#student_identifers = open("studentid.txt", "r")
#print(student_identifers.read())

#student_id_list = []
#student_id_list.append(student_identifers.read())
#print(student_id_list)

with open('assignment2file.txt') as f, open('studentid.txt') as f2:
    #if student_check in f.read():
        #print('Yes, student is there')

        #class Person:
            #def __init__(self, name):
                #self.name = name
                #self.identifier = identifier

        #p1 = Person(student_check)

        #print(p1.name)

    #else:
        #print('No, invalid')

    lines = f.readlines()
    lines_2 = f2.readlines()
    lns = [line.strip()for line in lines]
    lns_2 = [line.strip() for line in lines_2]

    lns = list(map(str, lns))
    lns_2 = list(map(int, lns_2))

    student_check = input("Please enter the name of the student you want to find: ")
    if student_check in lns:
        print(student_check)
        print(lns_2[lns.index(student_check)])