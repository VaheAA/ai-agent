import os

from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)

        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        dir_name = os.path.dirname(abs_full_path)

        os.makedirs(dir_name, exist_ok=True)

        if os.path.isdir(abs_full_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        with open(abs_full_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Function to write content to specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The directory where the agent should work.",
            ),
            "file_path": types.Schema(type=types.Type.STRING, description="Target file which should be edited. In case of non existing file, create one."),
            "content": types.Schema(type=types.Type.STRING, description="Content which should be written to the specified file.")
        },
    ),
)
