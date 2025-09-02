import os 

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if os.path.abspath(full_path).startswith(os.path.abspath(working_directory)) == True:
        pass
    else:
        return f'Error: Cannot list {directory} as it is outside the permitted working directory'
    if os.path.isdir(full_path) == False:
        return f'Error: {directory} is not a directory'
    content_list = []
    for content in os.listdir(full_path):
        content_path = os.path.join(full_path, content)
        file_size = os.path.getsize(content_path)
        is_dir = os.path.isdir(content_path) 
        data = f'- {content}: file_size={file_size}, is_dir={is_dir}'
        content_list.append(data)
    return "\n".join(content_list)
