import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\prank")
    print(file_list)
    #(2) for each file, rename filename

rename_files()