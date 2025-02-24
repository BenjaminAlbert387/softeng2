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
        def __init__(self, csv_file):
            # Initialize the class with the CSV file and read it into a DataFrame
            self.df = pd.read_csv(csv_file)
            # Remove leading/trailing spaces from column names
            self.df.columns = self.df.columns.str.strip()

        def find_module_columns(self, module_code):
            """
            Find the columns corresponding to the given module code.
            :param module_code: The module code to look for (e.g., 19901)
            :return: Tuple containing the names of the does_ and _grade columns
            """
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

        def filter_students(self, module_code):
            
            #Filters students based on the specified module code inputted and return their details

            #Parameter: 
            # module_code: The module code to filter by (e.g., 19901)

            #Returns: 
            # DataFrame with filtered students' details or None if columns not found
            
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
        print(f"Could not find columns for module code {module_code}")
        main2()

if __name__ == "__main__":
    OptionFunction()