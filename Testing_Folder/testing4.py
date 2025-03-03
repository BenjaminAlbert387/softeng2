def StudentFunction():
    student_option = input("Please input the student identitfier: ")
    open_file = open("demofile.txt", "rt")
    #print(open_file.read())

    for line in open_file:
                if str(student_option) in line.strip():
                    print("Student found!")
                    return True
                    
                
                else:
                     print("Student not found")
                     StudentFunction()
                StudentFunction()


def OptionFunction():
    first_option = input("Do you want to access students or modules: ").lower()
    
    if first_option == "students":
        first_option = True
        print("Loading students archive...")
        StudentFunction()
            
    elif first_option == "modules":
        first_option = True
        print("Loading modules")
    else:
        print("Try again!") 
        OptionFunction()    
OptionFunction()

open_file = open("demofile.txt", "rt")
print(open_file.read())
