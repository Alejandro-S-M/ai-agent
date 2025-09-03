import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_path_wdir = os.path.abspath(working_directory)
    abs_path_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_path_file.startswith(abs_path_wdir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_path_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_path_file, "r") as file:
            content_string = file.read(MAX_CHARS)
            if os.path.getsize(abs_path_file) > MAX_CHARS:
                content_string +=  f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content_string
    except Exception as e:
        return f'Error: {e}'
