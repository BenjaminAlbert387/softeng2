import csv
import pandas as pd

def OptionFunction():
    print("Type students, modules or averages.")
    first_option = input("Do you want to search students, modules or averages? ")

    if first_option == "students":
        main()
    elif first_option == "modules":
        main2()
    else:
        print("")
        print("Invalid option. Please try again.")
        OptionFunction()

def main():
    user_input = input("Enter the student ID you wish to search for: ")

    # open() opens the CSV file to be used

    #Parameters:
    # newline='': Matches the same format as the CSV file
    # mode='r': File is read only

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

def main2():
    class StudentModuleFilter:

        # __init__() is used to initalise a class

        #Parameters:
        # self: The first instance of the class
        # csv_file: The students_csv file 

        def __init__(self, csv_file):
            # Initialize the class with the CSV file and read it into a DataFrame
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
        # DataFrame with filtered students' details if the input matches
        # None if the user input doesn't match

        def filter_students(self, module_code):
            # Find the appropriate columns for the module
            does_column, grade_column = self.find_module_columns(module_code)
            if does_column and grade_column == True:
                # Filter the DataFrame to include only students taking the specified module
                filtered_students = self.df[self.df[does_column] == 'yes'][['userid', 'name', grade_column]].copy()
                return filtered_students
            else:
                return None

    csv_file = 'students.csv'
    module_code = input("Enter the module code (e.g., 19901): ")

    # Create an instance of the StudentModuleFilter class
    filter = StudentModuleFilter(csv_file)

    # Filter students based on the provided module code
    filtered_students = filter.filter_students(module_code)

    if filtered_students is not None:
        # Output the filtered students with Name, ID, and Grade
        print(filtered_students)
    else:
        print(f"Could not find modules with module code {module_code}")
        main2()

# Runs the OptionFunction() when the program starts 
if __name__ == "__main__":
    OptionFunction()