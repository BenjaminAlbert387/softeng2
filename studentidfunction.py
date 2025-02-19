def student_id_function():
    with open('studentid.txt') as file1:
        lines_1 = file1.readlines()
        lns = [line.strip() for line in lines_1]
        lns = list(map(int, lns))
        
        identifier_check = int(input("Please enter the ID number of the student you want to find: "))

        if identifier_check in lns:
            print(identifier_check)
            return identifier_check, lns

student_id_function()