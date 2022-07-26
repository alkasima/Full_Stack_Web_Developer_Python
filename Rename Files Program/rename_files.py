import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name: " + file_name)
        print("New Name: " + ''.join(i for i in file_name if not i.isnumeric()))
        os.rename(file_name, ''.join(i for i in file_name if not i.isnumeric()) )
    os.chdir(saved_path)

rename_files()