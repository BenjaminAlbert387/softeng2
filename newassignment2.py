import csv

def OptionFunction():
    print("Type students, modules or averages.")
    first_option = input("Do you want to search students, modules or averages? ")

    if first_option == "students":
        main()
    # elif first_option == "modules":
    #     main2()
    else:
        print("")
        print("Invalid option. Please try again.")
        OptionFunction()

def main():
    user_input = input("Enter the student ID you wish to search for: ")

    with open('students.csv', newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skips the header row of the CSV file

        found = False  # Flag to check if the ID was found
        for row in reader:
            if row[0] == user_input:
                print(row)
                print(f"Name: {row[1]}")
                print(f"Registered for programming module? {row[2]}")
                if row[2] == 'yes':
                    print(f"Programming grade: {row[3]}")
                else:
                    print("")

                print(f"Registered for ethics module? {row[4]}")
                if row[4] == 'yes':
                    print(f"Ethics grade: {row[5]}")
                else:
                    print("")

                print(f"Registered for maths module? {row[6]}")
                if row[6] == 'yes':
                    print(f"Maths grade: {row[7]}")
                else:
                    print("")

                found = True  # Set flag to true when ID is found
                break

        if not found:
            print("Invalid ID! Please try again.")
            main()

if __name__ == "__main__":
    OptionFunction()
