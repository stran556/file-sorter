# filesort / disperse.py

import os
import subprocess

# Preset source location and destination of disperse
loc1 = "/mnt/c/Users/Sean/Documents"
loc2 = "/mnt/c/Users/Sean/Desktop"
loc3 = "/mnt/c/Users/Sean/Desktop/bash/scripts/filesort"


# Disperse contents of directory to destination
def disperse(d):
    cmd2 = 'ls -p ' + loc1 + '\/' + d + ' > ' + loc3 + '\/' + 'lsfile.txt'
    os.system(cmd2)
    file2 = open(loc3 + "/lsfile.txt", "r")
    for name2 in file2:
        cmd3 = 'mv ' + loc1 + '\/' + d + '\/' + '\'' + name2.strip() + '\'' + ' ' + loc2
        os.system(cmd3)

    # Delete empty directory folder
    cmd4 = 'rmdir ' + loc1 + '\/' + d
    os.system(cmd4)


# Retrieve all directories in source location
cmd = 'ls -p ' + loc1 + ' | grep / | rev | cut -c 2- | rev > ' + loc3 + '\/' + 'lsfile.txt'
os.system(cmd)
file = open(loc3 + "/lsfile.txt", "r")
direc = []
for line in file:
    direc.append(line)


# Read user input until terminated
directory = " "
while directory != "":
    directory = input('')
    found = False
    for name in direc:
        if name.strip() == directory:
            found = True
    if found:
        disperse(directory)
    else:
        if directory != "":
            print(directory + ": Directory not found.")
        else:
            print("File dispersal terminated.")

os.system('> lsfile.txt')
