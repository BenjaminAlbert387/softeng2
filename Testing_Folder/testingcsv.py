import pandas as pd

# Read the CSV file
df = pd.read_csv('students.csv')
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names

# Print the column names to check for discrepancies
print("Column Names:", df.columns)

# Get module code from the user
module_code = input("Enter the module code (e.g., 19901): ")

# Function to find the correct columns based on user input
def find_module_columns(module_code):
    does_column = None
    grade_column = None
    for column in df.columns:
        if f'({module_code})' in column:
            if column.startswith('does_'):
                does_column = column
            elif '_grade' in column:
                grade_column = column
    return does_column, grade_column

# Find the correct columns
does_column, grade_column = find_module_columns(module_code)

# Print diagnostic information
print("Does Column:", does_column)
print("Grade Column:", grade_column)

if does_column and grade_column:
    # Filter students taking the specified module
    filtered_students = df[df[does_column] == 'yes'][['userid', 'name', grade_column]].copy()
    
    # Output the filtered students with Name, ID, and Grade
    print(filtered_students)
else:
    print(f"Could not find columns for module code {module_code}")

