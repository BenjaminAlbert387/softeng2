# testingfileinput.py

# Import the validation functions from validation.py
from validation import is_valid_student_option, read_valid_options

def main():
    file_path = "demofile.txt"
    
    # Read the valid student options from the file
    valid_student_options = read_valid_options(file_path)
    
    # Ensure valid_student_options is read correctly
    print(f"Valid student options: {valid_student_options}")
    
    # Get user input
    student_option = input("Please input the student identifier: ").strip()
    
    # Check if the input data is valid
    if is_valid_student_option(student_option, valid_student_options):
        print(f"Valid input: {student_option}")
    else:
        print(f"Invalid input: {student_option}")

if __name__ == "__main__":
    main()
