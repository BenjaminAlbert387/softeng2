import csv

def OptionFunction():
    print("Type students, modules or averages.")
    first_option = input("Do you want to search students, modules or averages? ")    

    if first_option == "students":
        main()

    #elif first_option == "modules":
        #main2()

    else:
        print("")
        print("Invalid option. Please try again.")
        OptionFunction()

def main():
    user_input = input("Enter the student ID you wish to search for: ")

    with open('students.csv', newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            if row[0] == user_input:
                print(row)
            else:
                print("Invalid ID!")
                main()

# Runs the OptionFunction() when the program starts
if __name__ == "__main__":
    OptionFunction()