import os
import shutil

from_dir = "C:/Users/Asus/Downloads"
to_dir = 'C:/Adithya/document_files'

list_of_files=os.listdir(from_dir)


for files in list_of_files:
    os.path.splitext(files)
    print(files)