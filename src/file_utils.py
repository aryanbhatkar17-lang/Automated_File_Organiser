import os
import shutil

def organise_files(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            folder = os.path.join(path,ext.upper() + "_Files")

            os.makedirs(folder, exist_ok= True)
            shutil.move(file_path, os.path.join(folder, filename))