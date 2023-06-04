import os
import shutil

to_dir = 'C:/Users/adity/OneDrive/Desktop'
from_dir = "C:/Users/adity/Downloads"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.png','.jpg','.jpeg','.gif','.jfif']:
        path_1 = from_dir + '/' + file_name
        print(path_1)
        path_2 = to_dir + '/' + 'screenshots'
        print(path_2)
        path_3 = to_dir + '/' + 'screenshots' + '/' + file_name
        print(path_3)
        if os.path.exists(path_2):
            print('Moving the',file_name,'...')
            shutil.move(path_1,path_3)
        else:
            os.mkdir(path_2)
            print('Creating a folder in the destination path')
            print('Moving the',file_name,'...')
            shutil.move(path_1,path_3)
