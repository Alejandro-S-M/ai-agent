from functions.get_files_info import get_files_info

def print_data(working_directory, directory):
    print(f' Result for current directory:\n {get_files_info(working_directory, directory)}')

print_data("calculator", ".")

print_data("calculator", "pkg")

print_data("calculator", "/bin")

print_data("calculator", "../")