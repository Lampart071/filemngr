from os import system, name
import shutil
import os


def set_path(info):
    print(info)
    path = input()
    flag_can_continue = False
    path, flag_can_continue = path_confirmation(path, flag_can_continue)
    if flag_can_continue:
        return path
    else:
        menu()

def set_format():
    print("Set file extenstion [without '.']: ")
    file_ext = "." + input()
    # TODO: Add whitespace and dot trimmning
    # TODO: Add extention confirmation
    return file_ext


def path_confirmation(path, flag_can_continue=False):
    print(path, " <-  is that a correct path? [(Y)es, (N)o]")
    confirmation_input = input()
    if confirmation_input == "Y":
        print("-> OK, proceed")
        flag_can_continue = True
    elif confirmation_input == "N":
        print("Set new directory: ")
        path = input()
        print(path, " <-  is that a correct path? [(Y)es, (N)o]")
        confirmation_input = input()
        if confirmation_input == "Y":
            print("-> OK, proceed")
            flag_can_continue = True
        elif confirmation_input == "N":
            flag_can_continue = False
    return path, flag_can_continue


def list_files():
    source_path = set_path("Set source directory: ")
    file_ext = set_format()
    file_count = 0
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(file_ext):
                path_file = os.path.join(root, file)
                print(path_file)
                file_count = file_count + 1
    print("\nFILE COUNT: ", file_count)
    return menu()


def copy_files():
    source_path = set_path("Set source directory: ")
    destination_path = set_path("Set destination directory: ")
    file_ext = set_format()
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(file_ext):
                path_file = os.path.join(root, file)
                # TODO: Add errors management
                shutil.copy2(path_file, destination_path)
    print("-> COPY DONE!")
    return menu()


def move_files():
    source_path = set_path("Set source directory: ")
    destination_path = set_path("Set destination directory: ")
    file_ext = set_format()
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(file_ext):
                path_file = os.path.join(root, file)
                # TODO: Add errors management
                shutil.move(path_file, destination_path)
    print("-> MOVE DONE!")
    return menu()


def select_operation_switch(argument):
    switcher = {
        "1": list_files,
        "2": copy_files,
        "3": move_files,
    }
    func = switcher.get(argument, lambda: 'Invalid')
    return func()


def menu():
    print("\n")
    print("MENU\n1. List files\n2. Copy files\n3. Move files\nYour selection [1-3] : ")
    print(select_operation_switch(input()))


if __name__ == "__main__":
    menu()
    # TODO: Add errors management
