import os 

def get_files_info(working_directory, directory="."): 
    try: 
        full_path = os.path.join(working_directory, directory)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full = os.path.abspath(full_path)
        if abs_full != abs_working_dir: 
            if not abs_working_dir.endswith(os.sep): 
                abs_working_dir += os.sep
            if not abs_full.startswith(abs_working_dir):  
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isdir(full_path) == False: 
            return f'Error: "{directory}" is not a directory'

        output = []
        for element in os.listdir(full_path): 
            output.append(f'- {element}: file_size={os.path.getsize(os.path.join(full_path, element))} bytes, is_dir={os.path.isdir(os.path.join(full_path, element))}')

        return "\n".join(output)

    except TypeError as e: 
        return f'Error: {e}'