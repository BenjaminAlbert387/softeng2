student_file = open("assignment2file.txt", "r")

student_check = input("Please enter the name of the student you want to find: ")

with open('assignment2file.txt') as f:
    if student_check in f.read():
        print('Yes, student is there')
    else:
        print('No, invalid')