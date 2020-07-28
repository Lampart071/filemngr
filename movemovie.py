import shutil
import os
import sys

source_path = os.getcwd() + "\\test"
destination_path = os.getcwd() + "\\modified"
format = ("mp4", "avi", "flv", "webm")


# Tests if dir exists
# If does not exist, may be created
# If dir will not be created, exit programme
def check_dir_exists(path):
    if os.path.isdir(path):
        print(path + " <- Path exists")
    else:
        print(path + " <- Path does not exist\n Want to create it? [(Y)es, (N)o]")
        confirmation_input = input()
        if confirmation_input == "Y":
            print("-> OK, proceed")
            os.mkdir(path)
        else:
            print("-> Process aborted\n")
            exit()


if __name__ == "__main__":
    check_dir_exists(source_path)
    check_dir_exists(destination_path)
    # Find all files with chosen extension
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(format):
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
