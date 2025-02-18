with open('studentid.txt') as file1, \
    open('studentnames.txt') as file2, \
    open('programmingmodule.txt') as file3, \
    open('ethicsmodule.txt') as file4:

    lines = file1.readlines()
    lines_2 = file2.readlines()
    lines_3 = file3.readlines()
    lines_4 = file4.readlines()

    lns = [line.strip()for line in lines]
    lns_2 = [line.strip() for line in lines_2]
    lns_3 = [line.strip() for line in lines_3]
    lns_4 = [line.strip() for line in lines_4]

    lns = list(map(int, lns))
    lns_2 = list(map(str, lns_2))
    lns_3 = list(map(int, lns_3))
    lns_4 = list(map(int, lns_4))

    def OptionFunction():
        print("Type students, modules or averages.")
        input("Do you want to search students, modules or averages? ")
    
    first_option = input("Do you want to search students, modules or averages? ")
    
if first_option == "students":
    first_option = True
    print("Loading students archive...")

    identifier_check = int(input("Please enter the ID number of the student you want to find: "))

    from mathsmodulefunction import maths_module_function

    if identifier_check in lns:
        print(identifier_check)
        print("Name: " + lns_2[lns.index(identifier_check)])
        print("Programming Module: " + str(lns_3[lns.index(identifier_check)]))
        print("Ethics Module: " + str(lns_4[lns.index(identifier_check)]))
        maths_module_function(identifier_check, lns)
    else:
        print("Invalid number")
    
else:
    print("Invalid option. Please try again.")
    OptionFunction()