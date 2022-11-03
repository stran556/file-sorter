# filesort / disperse.py

import os
import subprocess

# Preset source location and destination of disperse
loc1 = "/mnt/c/Users/Sean/Documents"
loc2 = "/mnt/c/Users/Sean/Desktop"
loc3 = "/mnt/c/Users/Sean/Desktop/bash/scripts/filesort"


def disperse(d):
    cmd2 = 'ls -p ' + loc1 + '\/' + d + ' > ' + loc3 + '\/' + 'lsfile.txt'
    os.system(cmd2)
    file2 = open(loc3 + "/lsfile.txt", "r")
    for name2 in file2:
        cmd3 = 'mv ' + loc1 + '\/' + d + '\/' + '\'' + name2.strip() + '\'' + ' ' + loc2
        os.system(cmd3)


cmd = 'ls -p ' + loc1 + ' | grep / | rev | cut -c 2- | rev > ' + loc3 + '\/' + 'lsfile.txt'
os.system(cmd)
file = open(loc3 + "/lsfile.txt", "r")
dir = []
for line in file:
    dir.append(line)

directory = " "
while directory != "":
    directory = input('')
    found = False
    for name in dir:
        if name.strip() == directory:
            found = True
    if found:
        disperse(directory)
    else:
        if(directory != ""):
            print("Directory not found.")
        else:
            print("File dispersal ended.")

os.system('> lsfile.txt')
