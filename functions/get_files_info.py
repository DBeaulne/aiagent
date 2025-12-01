import os

def get_files_info(working_directory, directory="."):

    if directory.startswith("/") or directory.startswith("../"):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    path = os.path.join(working_directory, directory)
    print(f"full path: {path}")

    absolute_path = os.path.abspath(path)
    print(f"absolute path: {absolute_path}")

    if os.path.isdir(absolute_path):
        contents = os.listdir(path)
        print(contents)

    
    return

