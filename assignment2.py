#*student_check = input("Please enter the name of the student you want to find: ")

#student_identifers = open("studentid.txt", "r")
#print(student_identifers.read())

#student_id_list = []
#student_id_list.append(student_identifers.read())
#print(student_id_list)

with open('studentid.txt') as file1, open('studentnames.txt') as file2:
    lines = file1.readlines()
    lines_2 = file2.readlines()

    lns = [line.strip()for line in lines]
    lns_2 = [line.strip() for line in lines_2]

    lns = list(map(int, lns))
    lns_2 = list(map(str, lns_2))
    print(lns)

    identifier_check = int(input("Please enter the ID number of the student you want to find: "))

    if identifier_check in lns:
        print(identifier_check)
        print("Name: " + lns_2[lns.index(identifier_check)])
    else:
        print("Invalid number")