import os

from google.genai import types
MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)

        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            file_size = os.path.getsize(abs_full_path)

            if file_size > MAX_CHARS:
                return file_content_string + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to read files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
            "file_path": types.Schema(type=types.Type.STRING, description="The target file content of which should be read and truncated. In case of non-existend file throws error")
        },
    ),
)
