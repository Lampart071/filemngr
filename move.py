import shutil
import os


def set_source_path():
    print("Set source directory: ")
    source_path = input()
    # TODO: Add path validation
    # TODO: Add path confirmation
    return source_path


def set_destination_path():
    print("Set destination directory: ")
    destination_path = input()
    # TODO: Add path validation
    # TODO: Add path confirmation
    return destination_path


def set_format():
    print("Set file extenstion [without '.']: ")
    file_ext = "." + input()
    # TODO: Add whitespace and dot trimmning
    # TODO: Add extention confirmation
    return file_ext


def list_files():
    source_path = set_source_path()
    file_ext = set_format()
    file_count = 0
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(file_ext):
                path_file = os.path.join(root, file)
                print(path_file)
                file_count = file_count + 1
    print("\nFILE COUNT: ", file_count, "\n\n")
    return menu()


def copy_files():
    source_path = set_source_path()
    destination_path = set_destination_path()
    file_ext = set_format()
    # TODO: Add process confirmation
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(file_ext):
                path_file = os.path.join(root, file)
                shutil.copy2(path_file, destination_path)
    return menu()


def move_files():
    source_path = set_source_path()
    destination_path = set_destination_path()
    file_ext = set_format()
    # TODO: Add process confirmation
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(file_ext):
                path_file = os.path.join(root, file)
                shutil.move(path_file, destination_path)
    return menu()


def switch(argument):
    switcher = {
        "1": list_files,
        "2": copy_files,
        "3": move_files,
    }
    func = switcher.get(argument, lambda: 'Invalid')
    return func()


def menu():
    print("MENU\n1. List files\n2. Copy files\n3. Move files\nYour selection [1-3] : ")
    print(switch(input()))

if __name__ == "__main__":
    menu()
    # TODO: Add errors management
