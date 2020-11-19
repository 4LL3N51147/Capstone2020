import os
import sys
from datetime import datetime

# List all files in a directory using scandir()
basepath = 'logs/'
with os.scandir(basepath) as entries:
    for entry in entries:
        print("Working on ", entry.name)
        if entry.is_file():
            with open(entry.path, "r") as f:
                lines = [line.strip() for line in f.readlines()]
                steps = [line.split(', ')[0].split(' at')[0] for line in lines]
                times = [line.split(', ')[1] for line in lines]
                
                times = [datetime.fromisoformat(time_str) for time_str in times]
                time_diffs = []
                for i in range(len(times)):
                    if i == 0:
                        time_diffs.append('0')
                    else:
                        time_diffs.append((times[i]-times[i-1]).total_seconds())

                with open(entry.path.replace(".log", ".csv"), "w") as new_file:
                    for i in range(len(steps)):
                        new_line = steps[i]+','+str(time_diffs[i])+'\n'
                        new_file.write(new_line)
                    new_file.close()
