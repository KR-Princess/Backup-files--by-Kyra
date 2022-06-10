import os
import shutil
import time

def main():
    print("This will delete all your files that are older than a specific time!")
    path= input("Enter the path for the folder you want to organize! ")
    days= int(input("How many days old files do you want to keep? "))

    no_of_deleted_folders=0
    no_of_deleted_files=0

    seconds_in_difference= time.time()-(days*24*60*60)


    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds_in_difference >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                no_of_deleted_folders= no_of_deleted_folders+1
            else:
                for folder in folders:
                    folder_path= os.path.join(root_folder, folder)
                    if seconds_in_difference >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        no_of_deleted_folders= no_of_deleted_folders+1
                for file in files:
                    file_path= os.path.join(root_folder, file)
                    if seconds_in_difference >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        no_of_deleted_files= no_of_deleted_files+1
    else:
        print("File path not found!!")

def remove_folder(path):
    if not shutil.rmtree(path):
        print("Folder is removed successfully")
    else:
        print("Unable to delete folders!")

def remove_file(path):
    if not os.remove(path):
        print("Files are deleted successfully!")
    else:
        print("Unable to delete files!")

def get_file_or_folder_age(path):
    ctime= os.stat(path).st_ctime
    return ctime

main()