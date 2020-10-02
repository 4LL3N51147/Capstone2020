import subprocess
import os

parent_directory = 'imgs'

for i in range(1, 6):
    print("--------{}--------\nTesting 1 face with 1,5 and 10 imgs".format(i))
    folders = ['1_Face_5_Img', '1_Face_10_Img']
    for folder_name in folders:
        mode = 'min'
        print("Currently running Fawkes with {} in {} mode for the {} time".format(folder_name, mode, i))
        logFilePath = os.path.join(os.path.expanduser('~'), folder_name+'_'+ mode+'_'+str(i)+'.log')
        if os.path.isdir(os.path.join(parent_directory, folder_name)):
            bashCommand = "python3 ./fawkes/protection.py -d {} -m {} > {}".format(os.path.join(parent_directory, folder_name), mode, logFilePath)
            process = subprocess.run(bashCommand, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            print("Log file saved to {}".format(logFilePath))