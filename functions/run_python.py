import os
import subprocess

from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)

        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(abs_full_path):
            return f'Error: File "{file_path}" not found.'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        command = ['python', abs_full_path] + args

        completed_process =  subprocess.run(command, capture_output=True, timeout=30, text=True)

        output_parts = []

        if completed_process.stdout:
            output_parts.append("STDOUT:\n" + completed_process.stdout.strip())
        if completed_process.stderr:
            output_parts.append("STDERR:\n" + completed_process.stderr.strip())

        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")

        if not output_parts:
            return "No output produced."


        return "n".join(output_parts)

    except subprocess.TimeoutExpired:
        return f'Error: Execution of "{file_path}" timed out after 30 seconds.'
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
            "file_path": types.Schema(type=types.Type.STRING, description="Target python file path which should be executed. Throws error if file not a valid python file or does not exist."),
            "args": types.Schema(type=types.Type.ARRAY, description="Array optinal arguments which could be passed to the function. Empty array by default.", items=types.Schema(type=types.Type.STRING))
        },
    ),
)
