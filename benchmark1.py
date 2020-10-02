import subprocess
import os

parent_directory = 'imgs'
modes = ['min', "low", "mid", "high"]
for i in range (1, 6):
    print("--------{}--------\nTesting 1 face 1 img with 4 modes".format(i))
    folder_name = '1_Face_1_Img'
    for mode in modes:
        print("Currently running Fawkes with {} in {} mode for the {} time".format(folder_name, mode, i))
        logFilePath = os.path.join(os.path.expanduser('~'), folder_name+'_'+mode+'_'+str(i)+'.log')
        if os.path.isdir(os.path.join(parent_directory, folder_name)):
            bashCommand = "python3 ./fawkes/protection.py -d {} -m {} > {}".format(os.path.join(parent_directory, folder_name), mode, logFilePath)
            process = subprocess.run(bashCommand, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            print("Log file saved to {}".format(logFilePath))
