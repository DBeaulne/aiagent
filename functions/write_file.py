import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    print(f'abs_file_path: {abs_file_path}')

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        try:
            abs_path_string = abs_file_path.split('/')
            print(f'new path text: {abs_path_string}')
            new_abs_path = join(abs_path_string)
            print(f'new abs path: {new_abs_path}')
            # os.makedirs(abs_file_path)
        except Exception as e:
            return f'Error creating directory {os.path.dirname(abs_file_path)}: {e}'

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'new content: {content}'
    
    except Exception as e:
        return f'Error: writing to file "{file_path}": {e}'
