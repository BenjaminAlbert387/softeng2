import csv
import pandas as pd
import sys

def OptionFunction():
    print("Type students, modules or averages. Type quit to end the program.")
    first_option = input("Do you want to search students, modules or averages? ").lower()

    if first_option.strip() == "students":
        SearchStudentFunction()
    elif first_option.strip() == "modules":
        SearchModuleFunction()
    elif first_option.strip() == "averages":
        OptionTwoFunction()
    elif first_option.strip() == "quit":
        sys.exit()
    else:
        print("")
        print("Invalid option. Please try again.")
        OptionFunction()

def ReturnFunction():
    print("Typing no will return you back to the menu")
    return_user_input = input("Do you want to find something else, students or modules? ").lower()

    if return_user_input == "students":
        SearchStudentFunction()
    
    elif return_user_input == "modules":
        SearchModuleFunction()

    elif return_user_input == "no":
        OptionFunction()

    else:
        print("Invalid option, try again")
        ReturnFunction()

def SearchStudentFunction():
    user_input = input("Enter the student ID you wish to search for: ")

    # open() opens the CSV file to be used

    #Parameters:
    # newline='': Matches the same format as the CSV file
    # mode='r': File is read only

    with open('students.csv', newline='', mode='r') as csvfile: #(Ricky, 2020)
        reader = csv.reader(csvfile)
        next(reader, None)  # Skips the header row of the CSV file

        found = False  # Flag to check if the ID was found

        for row in reader:
            if row[0] == user_input.strip():
                #print(row)
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

                print(f"Registered for Computer Systems module? {row[8]}")
                if row[8] == 'yes':
                    print(f"Computer Systems grade: {row[9]}")
                else:
                    print("")

                found = True  # Set flag to true when ID is found
                ReturnFunction()
                break
            
        if not found:
            print("Invalid ID! Please try again.")
            SearchStudentFunction()

def SearchModuleFunction():
    class StudentModuleFilter:

        # __init__() is used to initalise a class

        #Parameters:
        # self: The first instance of the class
        # csv_file: The students_csv file 

        def __init__(self, csv_file):
            # Initialize the class with the CSV file and read it into a DataFrame (Ajax1234, 2017)
            self.df = pd.read_csv(csv_file)
            # Remove white space from column names
            self.df.columns = self.df.columns.str.strip()

        #Function:
        # find_module_columns(): Used to verify whether the user input matches and is valid

        #Parameters:
        # self: The first instance of the class
        # module_code: The user input

        #Returns:
        # does_column: Tuple containing any columns that begin with does_
        # _grade column: Tuple containing any columns that contain _grade

        def find_module_columns(self, module_code):
            does_column = None
            grade_column = None
            # Iterate over the column names to find matching ones
            for column in self.df.columns:
                if f'({module_code})' in column:
                    if column.startswith('does_'):
                        does_column = column
                    elif '_grade' in column:
                        grade_column = column
            return does_column, grade_column
        
        #Function:
        # filter_students(): Filters students based on the module code inputted

        #Parameter: 
        # module_code: The module code to filter by

        #Returns: 
        # DataFrame with filtered students' details if the user input matches
        # None if the user input doesn't match

        def filter_students(self, module_code):
            # Find the appropriate columns for the module
            does_column, grade_column = self.find_module_columns(module_code)
            if does_column and grade_column:
                # Filter the DataFrame to include only students taking the specified module
                # If the row contains yes, then copy the user ID, name and grade to the class
                filtered_students = self.df[self.df[does_column] == 'yes'][['userid', 'name', grade_column]].copy()
                return filtered_students
            else:
                return None

    csv_file = 'students.csv'
    module_code = input("Enter the module code: ")

    # Create an instance of the StudentModuleFilter class
    filter = StudentModuleFilter(csv_file)

    # Filter students based on the provided module code
    filtered_students = filter.filter_students(module_code)

    if filtered_students is not None:
        # Output the filtered students with Name, ID, and Grade
        print(filtered_students)
        ReturnFunction()
    else:
        print(f"Could not find modules with module code {module_code}")
        SearchModuleFunction()

def OptionTwoFunction():
    print("Type students or modules.")
    second_option = input("Do you want the average of all students or all modules? ").lower()

    if second_option.strip() == "students":
        StudentAveragesFunction()
    elif second_option.strip() == "modules":
        ModuleAveragesFunction()
    else:
        print("")
        print("Invalid option. Please try again.")
        OptionTwoFunction()

def StudentAveragesFunction():
    # Reads in the CSV file, only using columns with grades
    df = pd.read_csv('students.csv',usecols=[3, 5, 7, 9])

    # Reads in the CSV file, only uses the columns with student names and ID
    df2 = pd.read_csv('students.csv', usecols=[0, 1])

    # Calculates the mean of selected rows
    row_averages = df.mean(axis=1)

    print("Averages for each student: ")

    # Concatonates the DataFrame and Series together    
    df3 = pd.concat([df2, row_averages], axis=1)

    # Removes the 'dtype: float64' from the output (warkitty, 2019)
    # Also removes the header from the the output (BioData41, 2022)
    print(df3.to_string(header=False))
    ReturnFunction()

def ModuleAveragesFunction():
    # Reads in the CSV file, only using columns with grades
    df = pd.read_csv('students.csv',usecols=[3, 5, 7, 9])

    # Calculates the mean of selected columns
    column_averages = df.mean(axis=0)

    print("Averages for each module: ")

    # Removes the 'dtype: float64' from the output (warkitty, 2019)
    print(column_averages.to_string())
    ReturnFunction()

# Runs the OptionFunction() when the program starts 
if __name__ == "__main__":
    OptionFunction()

# References (Code Specific)
# warkitty (2019) ‘Answer to “How do I remove name and dtype from pandas output”’, Stack Overflow. Available at: https://stackoverflow.com/a/59182999 (Accessed: 25 February 2025).
# Ajax1234 (2017) ‘Answer to “How to read the contents of a csv file into a class with each csv row as a class instance”’, Stack Overflow. Available at: https://stackoverflow.com/a/47445846 (Accessed: 24 February 2025).
# BioData41 (2022) ‘Answer to “How to remove Header Row from DataFrame Output”’, Stack Overflow. Available at: https://stackoverflow.com/a/70546756 (Accessed: 25 February 2025).
# Ricky (2020) ‘Answer to “What does the argument newline=’’ do in the open function?”’, Stack Overflow. Available at: https://stackoverflow.com/a/61861566 (Accessed: 24 February 2025).


