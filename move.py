import shutil
import readchar
import os


def set_source_path():
    print("Set source directory: ")
    source_path = input()
    return source_path


def set_destination_path():
    print("Set destination directory: ")
    destination_path = input()
    return destination_path


def set_format():
    print("Set file extenstion [without '.']: ")
    file_ext = "." + input()
    return file_ext


def list_files():
    source_path = set_source_path()
    file_ext = set_format()
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(file_ext):
                path_file = os.path.join(root, file)
                print(path_file)


def copy_files():
    source_path = set_source_path()
    destination_path = set_destination_path()
    file_ext = set_format()
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(file_ext):
                path_file = os.path.join(root, file)
                shutil.copy2(path_file, destination_path)


def move_files():
    source_path = set_source_path()
    destination_path = set_destination_path()
    file_ext = set_format()
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(file_ext):
                path_file = os.path.join(root, file)
                shutil.move(path_file, destination_path)


def switch(argument):
    switcher = {
        "1": list_files,
        "2": copy_files,
        "3": move_files,
    }
    func = switcher.get(argument, lambda: 'Invalid')
    return func()


if __name__ == "__main__":
    print("MENU\n1. List files\n2. Copy files\n3. Move files\nYour selection [1-3] : ")
    print(switch(input()))
