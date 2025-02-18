def student_id_function():
    with open('studentid.txt') as file1:
        lines_1 = file1.readlines()
        lns = [line.strip() for line in lines_1]
        lns = list(map(int, lns))
        
        identifier_check = int(input("Please enter the ID number of the student you want to find: "))

        if identifier_check in lns:
            print(identifier_check)
            return identifier_check, lns

def maths_module_function(identifier_check, lns):
    with open('ethicsmodule.txt') as file5:
        lines_5 = file5.readlines()
        lns_5 = [line.strip() for line in lines_5]
        lns_5 = list(map(int, lns_5))
        
        if identifier_check in lns:
            #print("Maths Module: " + str(lns_5[lns.index(identifier_check)]))
            return str(lns_5[lns.index(identifier_check)])
        else:
            print("Invalid")

identifier_check, lns = student_id_function()
if identifier_check is not None:
    maths_module_function(identifier_check, lns)