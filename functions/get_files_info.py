import os

from google.genai import types

def get_files_info(working_directory, directory="."):

    try:
        full_path = os.path.join(working_directory, directory)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)

        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'

        contents = os.listdir(abs_full_path)

        output_lines = []

        for item in contents:
            item_path = os.path.join(abs_full_path, item)
            directory_name = 'current' if directory == '.' else directory
            is_dir = os.path.isdir(item_path)

            try:
                size = os.path.getsize(item_path)
            except (OSError, FileNotFoundError):
                size = 0

            output_lines.append(f" - {item}: file_size={size} bytes, is_dir={is_dir}")


        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
