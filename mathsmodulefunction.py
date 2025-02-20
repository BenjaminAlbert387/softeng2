from studentidfunction import student_id_function

def use_id():
    identifier_check = student_id_function(lns)

if __name__ == "__main__":
    use_id()

def maths_module_function(identifier_check, lns):
    with open('mathsmodule.txt') as file5:
        lines_5 = file5.readlines()
        lns_5 = [line.strip() for line in lines_5]
        lns_5 = list(map(int, lns_5))
        
        if identifier_check in lns:
            print("Maths Module: " + str(lns_5[lns.index(identifier_check)]))
            return str(lns_5[lns.index(identifier_check)])
        else:
            print("Invalid")

identifier_check, lns = student_id_function()
#if identifier_check is not None:
    #maths_module_function(identifier_check, lns)