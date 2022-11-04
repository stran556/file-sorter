#!/bin/bash

input="'$*'"

if [[ ${input} == *"--help"* ]]; then
	echo "Hello there"
elif [[ ${input} == *"-s"* ]]; then
	python3 '/mnt/c/Users/Sean/Desktop/bash/scripts/filesort/sort.py'
elif [[ ${input} == *"-d"* ]]; then
	python3 '/mnt/c/Users/Sean/Desktop/bash/scripts/filesort/disperse.py'
elif [[ -z ${1+x} ]]; then
	echo "No argument found. Use 'filesort --help' for assistance."
else
	echo "Unknown argument. Use 'filesort --help' for assistance."
fi
