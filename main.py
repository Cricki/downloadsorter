#!/usr/bin/python3
import os

path = os.path.expanduser('~/Downloads')

b = [name for name in os.listdir(path)]
print(b)


