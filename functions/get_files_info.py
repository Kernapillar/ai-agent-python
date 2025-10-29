import os 

def get_files_info(working_directory, directory="."): 
    full_path = os.path.join(working_directory, directory)
    if os.path.isdir(full_path) == False: 
        return f'Error: "{directory}" is not a directory'
    