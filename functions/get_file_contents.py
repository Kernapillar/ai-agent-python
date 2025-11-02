import os
from config import FILE_CHARACTER_LIMIT 

def get_file_content(working_directory, file_path): 
    try: 
        full_path = os.path.join(working_directory, file_path)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full = os.path.abspath(full_path)

        if not abs_working_dir.endswith(os.sep): 
            abs_working_dir += os.sep
        if not abs_full.startswith(abs_working_dir):  
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path): 
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_path, "r") as f: 
            file_content_str = f.read(FILE_CHARACTER_LIMIT + 1)
            if len(file_content_str) > FILE_CHARACTER_LIMIT:
                file_content_str = file_content_str[:FILE_CHARACTER_LIMIT] + f'[...File "{file_path}" truncated at 10000 characters]'
        
        return file_content_str

    except BaseException as e: 
        return f'Error: {e}'