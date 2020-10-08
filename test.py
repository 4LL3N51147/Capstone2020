import os
import sys
import fileinput

# List all files in a directory using scandir()
basepath = 'logs/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            for i, line in enumerate(fileinput.input(entry.path, inplace=1)):
                    sys.stdout.write(line.replace(':', ',', 1))