# validation.py

def is_valid_student_option(student_option, valid_options):
    """Check if the student_option is in the list of valid options."""
    return student_option in valid_options

def read_valid_options(file_path):
    """Read the list of valid student options from the file."""
    try:
        with open(file_path, "r") as file:
            valid_options = eval(file.read().strip())
            return valid_options
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except SyntaxError:
        print("Error reading file content.")
        return []
