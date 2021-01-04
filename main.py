#!/usr/bin/python3
import os
from os import listdir, walk
from os.path import isfile, join

#path = os.path.expanduser('~/Downloads')
#username = str(os.getlogin()) 
path = os.path.expanduser('/mnt/c/Users/bt199/Downloads')
d_folder = [name for name in os.listdir(path)]

files = []
folders = []

for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
    folders.extend(dirnames)
    break

print(files)
print(folders)
