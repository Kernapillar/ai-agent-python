import os
from google.genai import types

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
    


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write the contents of a specific file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath of the target file, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the specified file",
            ),
        },
    ),
)


