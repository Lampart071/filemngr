import shutil
import readchar
import os


def set_source_path():
    return


def set_destination_path():
    return


def set_format():
    return


def list_files():
    src = set_source_path()
    format = set_format()
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(format):
                path_file = os.path.join(root, file)
                print(path_file)


def copy_files():
    src = set_source_path()
    dest = set_destination_path()
    format = set_format()
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(format):
                path_file = os.path.join(root, file)
                shutil.copy2(path_file, dest)


def move_files():
    src = set_source_path()
    dest = set_destination_path()
    format = set_format()
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(format):
                path_file = os.path.join(root, file)
                shutil.move(path_file, dest)


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
    selection = input()
    print(switch(selection))
