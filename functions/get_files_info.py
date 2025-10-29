import os 

def get_files_info(working_directory, directory="."): 
    try: 
        full_path = os.path.join(working_directory, directory)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full = os.path.abspath(full_path)
        if abs_full.startswith(abs_working_dir) == False: 
            return f'Error: "Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.exists(full_path) == False: 
            return f'Error: "{full_path}" is not a valid path'
        if os.path.isdir(full_path) == False: 
            return f'Error: "{directory}" is not a directory'
        

    except TypeError as e: 
        return f'Error: {e}'