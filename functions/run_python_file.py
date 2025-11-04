import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]): 
    try: 
        full_path = os.path.join(working_directory, file_path)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full = os.path.abspath(full_path)

        if not abs_working_dir.endswith(os.sep): 
            abs_working_dir += os.sep
        if not abs_full.startswith(abs_working_dir):  
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_path): 
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith(".py"): 
            return f'Error: "{file_path}" is not a Python file.'
        
        completed_process = subprocess.run(args=["python", file_path, *args], timeout=30, capture_output=True, cwd=working_directory, text=True, )

        stdout = (completed_process.stdout or "").rstrip()
        stderr = (completed_process.stderr or "").rstrip()
        exit_code = f'\nProcess exited with code {completed_process.returncode}' if completed_process.returncode != 0 else ""
        
        if stdout == "" and stderr == "" and completed_process.returncode == 0: 
            return "No output produced."

        return f'STDOUT: {stdout}\nSTDERR: {stderr}{exit_code}'

    except BaseException as e: 
        return f'Error: executing Python file: {e}'
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Attempts to run the specified python file with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath of the target file, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional argument strings to pass to the file at runtime ",
            ),
        },
        required=["file_path"],
    ),
)

