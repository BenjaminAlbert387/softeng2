my_file = open("assignment2file.txt", "r")

data = my_file.read()

Students = data.split("\n")
for element in Students:
    specific = element.split()
    StudentName = specific[0]
    StudentID = specific[1]

print(Students)
print(element)
print("Student Name: " + StudentName, "StudentID: " + StudentID)
my_file.close()

