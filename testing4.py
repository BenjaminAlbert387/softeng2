def OptionFunction():
    students = ["Adam", "Billy", "Carl"]
    grades = ["50", "38", "77"]
    
    first_option = input("Do you want to access students or modules: ").lower()
    
    #while first_option == False:
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

