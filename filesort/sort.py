import os
import subprocess

# Preset source location and destination of sort
loc1 = "/mnt/c/Users/Sean/Desktop"
loc2 = "/mnt/c/Users/Sean/Documents"

cmd = 'ls -p ' + loc1 + ' | grep -v / > lsfile.txt'

file = open("lsfile.txt", "r")
print(file.read())

file_dir = []

for line in file:

    line = line[:-1]
    if line == "":
        break
    else:
        add_file_dir(line)


def add_file_dir(name):
    file_type = name[name.rfind("."):]
    # os.system(file_type + ' > output.txt')
    print(file_type)
