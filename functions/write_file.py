import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        try:
            rel_path = os.path.join(working_directory, file_path)
            path_dir = os.path.dirname(rel_path)
            os.makedirs(path_dir, exist_ok=True)
        except Exception as e:
            return f'Error creating directory {os.path.dirname(new_rel_path)}: {e}'

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: writing to file "{file_path}": {e}'
