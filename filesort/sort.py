import os
import subprocess

# Preset source location and destination of sort
loc1 = "input source here"
loc2 = "input destination here"
loc3 = "input file-sort location here"

cmd = 'ls -p ' + loc1 + ' | grep -v / > ' + loc3 + '\/'  + 'lsfile.txt'
os.system(cmd)
file = open(loc3 + "/lsfile.txt", "r")
file_dir = []


# Transfers directories from source to destination after all files are sorted
def transfer_file_dir():
    for file_t in file_dir:
        cmd3 = 'mv ' + loc1 + '/' + file_t + ' ' + loc2
        os.system(cmd3)


# Creates directories if none are found
def add_file_dir(name):
    file_type = name[name.rfind(".") + 1:]
    found = False
    for f_type in file_dir:
        if f_type == file_type:
            found = True
            continue
    if not found:
        file_dir.append(file_type)

        # directory is created in source if necessary
        cmd2 = 'mkdir ' + loc1 + '/' + file_type
        os.system(cmd2)

    return file_type


for line in file:
    line = line[:-1]
    file_type3 = add_file_dir(line)

    # mv /mnt/c/Users/Sean/Desktop/file.pdf /mnt/c/Users/Sean/Desktop/pdf
    cmd4 = 'mv ' + loc1 + '/' + '\'' + line + '\'' + ' ' + loc1 + '/' + file_type3
    os.system(cmd4)

transfer_file_dir()
