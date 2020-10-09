import os
import sys
import fileinput

# List all files in a directory using scandir()
basepath = 'logs_2/'
with os.scandir(basepath) as entries:
    for entry in entries:
        print(entry.name)
        if entry.is_file():
            for i, line in enumerate(fileinput.input(entry.path, inplace=1)):
                    if '2020' in line:
                        if 'processing' in line:
                            line = line.replace('at', 'at:', 1)
                        sys.stdout.write(line.replace(':', ',', 1))