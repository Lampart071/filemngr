import sys
import shutil
import os


# Set the path will be used
# Check process confirmation flag
def set_path(info):
    print(info)
    path = input()
    flag_can_continue = False
    path, flag_can_continue = path_confirmation(path, flag_can_continue)
    if flag_can_continue:
        return path
    else:
        menu()


# Set file extension you want to proceed with
def set_extension():
    print("Set file extension [without '.']: ")
    file_ext = "." + input()
    # TODO: Add whitespace and dot trimmning
    # TODO: Add extension confirmation
    return file_ext


#  Confirm selected data to proceed
def process_confirmation(path_src, path_dest, extension):
    print(path_src, " <- Source path")
    print(path_dest, " <- Destination path")
    print(extension, " <- Extension")
    print("Continue process? [(Y)es, (N)o]")
    confirmation_input = input()
    if confirmation_input == "Y":
        print("-> OK, proceed")
        flag_can_continue = True
    else:
        print("-> Process aborted\n")
        flag_can_continue = False
    return flag_can_continue


# Confirm selected path is correct
# Change path if incorrect
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


#  List all the files in directory ending with chosen extension
def list_files():
    source_path = set_path("Set source directory: ")
    file_ext = set_extension()
    file_count = 0
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(file_ext):
                path_file = os.path.join(root, file)
                print(path_file)
                file_count = file_count + 1
    print("\nFILE COUNT: ", file_count, "\n")
    return menu()


# Copy files with chosen extension to selected directory
def copy_files():
    # Set and confirm if chosen path is correct
    source_path = set_path("Set source directory: ")
    destination_path = set_path("Set destination directory: ")
    # Set searched file extension
    file_ext = set_extension()
    # Find all files with chosen extension
    if process_confirmation(source_path, destination_path, file_ext):
        for root, dirs, files in os.walk(source_path):
            for file in files:
                if file.endswith(file_ext):
                    path_file = os.path.join(root, file)
                    try:
                        # Copy file to chosen directory
                        shutil.copy2(path_file, destination_path)
                        print(path_file, " -> ", destination_path, " [COPY DONE!]\n")
                    except OSError as err:
                        print("OS error: {0}".format(err), "\n")
                    else:
                        e = sys.exc_info()[0]
                        print("Unexpected error:", sys.exc_info()[0], "\n")
        return menu()
    else:
        return menu()


# Move files with chosen extension to selected directory
def move_files():
    # Set and confirm if chosen path is correct
    source_path = set_path("Set source directory: ")
    destination_path = set_path("Set destination directory: ")
    # Set searched file extension
    file_ext = set_extension()
    # Find all files with chosen extension
    if process_confirmation(source_path, destination_path, file_ext):
        for root, dirs, files in os.walk(source_path):
            for file in files:
                if file.endswith(file_ext):
                    path_file = os.path.join(root, file)
                    try:
                        # Move file to chosen directory
                        shutil.move(path_file, destination_path)
                        print(path_file, " -> ", destination_path, " [MOVE DONE!]\n")
                    except OSError as err:
                        print("OS error: {0}".format(err), "\n")
                    else:
                        e = sys.exc_info()[0]
                        print("Unexpected error:", sys.exc_info()[0], "\n")
        return menu()
    else:
        return menu()


#  Menu switch
def select_operation_switch(argument):
    switcher = {
        "1": list_files,
        "2": copy_files,
        "3": move_files,
        "Q": exit
    }
    func = switcher.get(argument, lambda: 'Invalid\n')
    return func()


#  Menu list
#  Proceed to Menu switch
def menu():
    print("MENU\n1. List files\n2. Copy files\n3. Move files\nQ. Quit\nYour selection [1-3,Q] : ")
    print(select_operation_switch(input()))


if __name__ == "__main__":
    menu()

# 1. find all movie formats
# 2. create and move movies to current directory inside the folder
# 3. duplicates?
# 4. Cut out presented strings from filename
