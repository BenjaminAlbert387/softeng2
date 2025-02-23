# Import necessary functions from other files
from ethicsmodulefunction import ethics_module_function
from mathsmodulefunction import maths_module_function

# load_function() loads data from a file and convert each line to a string datatype

#Parameters:
#file_path (str): Path to the file, for example studentid.txt
#datatype (type): Type to which each line should be converted

#Returns a list of converted lines from the file as strings

def load_file(file_path, datatype=str):
    with open(file_path) as file:
        return [datatype(line.strip()) for line in file.readlines()]

def load_data():

# load_data() loads data from multiple files

#Returns a tuple: Contains lists of student IDs, student names and grades for each module

    student_ids = load_file('studentid.txt', int)
    student_names = load_file('studentnames.txt')
    programming_grades = load_file('programmingmodule.txt', int)
    module_codes = load_file('modulecode.txt')
    return student_ids, student_names, programming_grades, module_codes

def validate_student_id(student_id, student_ids):
    
# validate_student_id() checks if the provided student ID exists in the list of student IDs.
    
#Parameters:
#student_id (int): The student ID to validate
#student_ids (list): List of valid student IDs

#Returns a boolean: True if the student ID is valid, False otherwise
    
    return student_id in student_ids

def validate_module_code(module_code, module_codes):
    
# validate_module_code() checks if the provided module code exists in the list of module codes.
    
#Parameters:
#module_code (int): The module code to validate, inputted by the user
#student_ids (list): List of module codes

#Returns a boolean: True if the module code is valid, False otherwise
    
    return module_code in module_codes

def display_student_info(student_id, student_ids, student_names, programming_grades):
    
# display_student_info() outputs the student's information

#Parameters:
#student_id (int): The student ID to display information for
#student_ids (list): List of student IDs
#student_names (list): List of student names corresponding to the student IDs
#programming_grades (list): List of programming module grades corresponding to the student IDs
    
    index = student_ids.index(student_id)
    print(f"Student ID is valid!")
    print(f"Name: {student_names[index]}")
    print(f"Programming Module Grade: {programming_grades[index]}")

def display_module_info(module_id, module_ids, student_names):
    print(f"Called display_module_info with module_id: {module_id}")
    index = module_ids.index(module_id)
    print(f"Module code is valid!")
    print(f"Name: {student_names[index]}" + f"Grade: {module_ids[index]}")

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

    student_ids, student_names, programming_grades, module_codes = load_data()
    user_input = int(input("Enter the student ID you wish to search for: "))
    
    if validate_student_id(user_input, student_ids):
        display_student_info(user_input, student_ids, student_names, programming_grades)
        ethics_module_function(user_input, student_ids)
        maths_module_function(user_input, student_ids)
    else:
        print("Invalid student ID")

def main2():

    student_ids, student_names, programming_grades, module_codes = load_data()
    user_input = int(input("Enter the module ID you wish to search for: "))

    if validate_module_code(user_input, module_codes):
        display_module_info(user_input, student_names, module_codes)


# Runs the OptionFunction() when the program starts
if __name__ == "__main__":
    OptionFunction()
