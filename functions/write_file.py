import os

def write_file(working_directory, file_path, content): 
    try: 
        full_path = os.path.join(working_directory, file_path)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full = os.path.abspath(full_path)

        if not abs_working_dir.endswith(os.sep): 
            abs_working_dir += os.sep
        if not abs_full.startswith(abs_working_dir):  
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        with open(full_path, "w") as f: 
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except BaseException as e: 
        return f'Error: {e}'