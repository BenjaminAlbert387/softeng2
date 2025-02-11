def OptionFunction():
    first_option = input("Do you want to access students or modules: ").lower()
    
    if first_option == "students":
        first_option = True
        print("Loading students archive...")
            
    elif first_option == "modules":
        first_option = True
        print("Loading modules")
    else:
        print("Try again!") 
        OptionFunction()    
OptionFunction()

open_file = open("demofile.txt", "rt")
print(open_file.read())