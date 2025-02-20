from studentidfunction import student_id_function

def use_id():
    identifier_check = student_id_function()

if __name__ == "__main__":
    use_id()

def ethics_module_function(identifier_check, lns):
    with open('ethicsmodule.txt') as file4:
        lines_4 = file4.readlines()
        lns_4 = [line.strip() for line in lines_4]
        lns_4 = list(map(int, lns_4))
        
        if identifier_check in lns:
            print("Ethics Module: " + str(lns_4[lns.index(identifier_check)]))
            return str(lns_4[lns.index(identifier_check)])
        else:
            print("Invalid")

identifier_check, lns = student_id_function()