import os
import sys
from datetime import datetime

# List all files in a directory using scandir()
basepath = '8_thread/'
test_subjs = ["1_Face_1_Img_high", "1_Face_1_Img_low", "1_Face_1_Img_mid","1_Face_1_Img_min","1_Face_5_Img_min", "1_Face_10_Img_min", "4_Face_1_Img_min"]
for test_subj in test_subjs:
    steps = []
    times = []
    with open(basepath+test_subj+".csv", "w") as result:
        for i in range(1, 6):
            filename = basepath+test_subj+"_"+str(i)+".csv"
            with open(filename, "r") as f:
                lines = [line.strip() for line in f.readlines()]
                steps = [line.split(',')[0] for line in lines]
                times.append([line.split(',')[1] for line in lines])
        for i in range(len(steps)):
            newline = steps[i]
            for time in times:
                newline += ","+time[i]
            newline += "\n"
            result.write(newline)
        result.close()