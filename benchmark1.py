import subprocess
import os

parent_directory = 'imgs'
modes = ['min', "low", "mid", "high"]

print("--------1--------\nTesting 1 face 1 img with 4 modes")
folder_name = '1_Face_1_Img'
for mode in modes:
    print("Currently running Fawkes with {} in {} mode".format(folder_name, mode))
    logFilePath = os.path.join(os.path.expanduser('~'), folder_name+'_'+ mode+'.log')
    if os.path.isdir(os.path.join(parent_directory, folder_name)):
        bashCommand = "python3 ./fawkes/protection.py -d {} -m {} > {}".format(os.path.join(parent_directory, folder_name), mode, logFilePath)
        process = subprocess.run(bashCommand, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        print("Log file saved to {}".format(logFilePath))