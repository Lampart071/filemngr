import shutil
import os

# src = "D://UT//VID"
# dest = "D://UT//VIDMOVE"
# format = "." + "mp4"
#
# def set_source_path():
#
# def set_destination_path():
#
# def set_format():
#
#
# def list_files(src, format):
#     for root, dirs, files in os.walk(src):
#         for file in files:
#             if file.endswith(format):
#                 path_file = os.path.join(root, file)
#                 print(path_file)
#
# def copy_files(src, dest, format):
#     for root, dirs, files in os.walk(src):
#         for file in files:
#             if file.endswith(format):
#                 path_file = os.path.join(root, file)
#                 shutil.copy2(path_file, dest)
#
# def move_files(src, dest, format):
#     for root, dirs, files in os.walk(src):
#         for file in files:
#             if file.endswith(format):
#                 path_file = os.path.join(root, file)
#                 shutil.move(path_file, dest)

def main(self, context):
    print("MENU\n1. List files\n2. Copy files\n3. Move files\nYour select[1-3]: ")
