import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\message")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\message")
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old File Name: " + file_name)
        print("New File Name: " + ''.join(i for i in file_name if not i.isnumeric()))
        os.rename(file_name, ''.join(i for i in file_name if not i.isnumeric()) )
    os.chdir(saved_path)

rename_files()