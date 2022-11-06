# file-sorter

Deep computer work often leads to excessive clutter on your desktop. Text files over here, mp4 files over there, png's and pdf's everywhere. You don't want to waste your precious time dragging files around with your cursor in hopes of establishing even a little bit of order amongst all the chaos. So what can you do?

Filesort cleans your desktop for you by organizing files into directories by format type (pdf, jpg, txt, etc.) and moving them into a location of your choice.

Fill in the preset values 'loc1' and 'loc2' for the source and destination in 'sort.py' and 'disperse.py'. Filesort will do the rest.

## fs -s

Sort files from a source location into directories in the destination

## fs -d

Disperse folders one-by-one from a source location into the destination

This program interlaps Python3 with Linux system calls to accomplish the sorting task. If directories for a file format are already found in the destination directory, they will be sorted into files, but will not be transferred from the source. If directories are already found in the source but not the destination, the files will still be sorted and transferred.

###Tools that may need installation: 
Python3- Running .py files (sort, disperse)
