students = ["Adam", "Billy", "Carl"]
grades = ["50", "38", "77"]

print(students[0] + " " + grades [0])

def OptionFunction():
    input("Do you want to access students or modules: ")

first_option = input("Do you want to access students or modules: ")
    
if first_option == "students":
    first_option = True
    print("Loading students archive...")
        
elif first_option == "modules":
    first_option = True
    print("Loading modules")
    
else:
    print("Invalid option. Please try again.")
    OptionFunction()