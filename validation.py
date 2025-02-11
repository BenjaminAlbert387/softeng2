# validation.py

def is_valid_student_option(student_option, valid_options):
    """Check if the student_option is in the list of valid options."""
    return student_option in valid_options

def read_valid_options(file_path):
    """Read the list of valid student options from the file."""
    try:
        with open(file_path, "r") as file:
            # Execute the file content to get the variable
            global_vars = {}
            exec(file.read(), global_vars)
            valid_options = global_vars.get('student_options', [])
            return valid_options
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file content: {e}")
        return []