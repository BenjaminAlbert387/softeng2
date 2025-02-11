# validation.py
import ast

def is_valid_student_option(student_option, valid_options):
    """Check if the student_option is in the list of valid options."""
    return student_option in valid_options

def read_valid_options(file_path):
    """Read the list of valid student options from the file."""
    try:
        with open(file_path, "r") as file:
            content = file.read()
            # Extract the student_option list from the content
            start = content.find("student_option = [")
            end = content.find("]", start) + 1
            student_option_list_str = content[start + len("student_option = "):end]
            valid_options = ast.literal_eval(student_option_list_str.strip())
            return valid_options
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except (SyntaxError, ValueError):
        print("Error reading file content.")
        return []

