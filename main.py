#!/usr/bin/python3
import os
import pathlib
import time
from datetime import datetime
from os import listdir, walk
from os.path import isfile, join

home = os.path.expanduser("~")
path = os.path.expanduser('~/Downloads')
#username = str(os.getlogin()) 
#path = os.path.expanduser('/mnt/c/Users/bt199/Downloads')

def get_download_folder() -> str:
    home = os.path.expanduser("~")
    return os.path.join(home, "Downloads")

def sub_folder(extension: str) -> str:
    download = get_download_folder()
    return os.path.join(download, extension)

def check_and_create_folders(folders):
    for x in folders:
        sub = sub_folder(x)
        if not os.path.exists(sub):
            os.makedirs(sub)

def get_suitable_folder(f: str) -> str:
    print(f)
    ext = f[f.find("."):]
    print(ext)


def move_files():
    for x in exist_files:
        date = datetime.fromtimestamp(os.path.getctime(os.path.join(path, x)))
        datediff = datetime.today() - date
        get_suitable_folder(x)
        #if datediff.days > 5:
            #os.rename(os.path.join(path, x), os.path.join(path, sub, x))

#d_folder = [name for name in os.listdir(path)]

exist_files = []
exist_folders = []
for (dirpath, dirnames, filenames) in walk(path):
    exist_files.extend(filenames)
    exist_folders.extend(dirnames)
    break

foldernames  = ["pdf", "docx", "img", "exe", "zip"]
check_and_create_folders(foldernames)
move_files()


