import subprocess
import os

parent_directory = 'imgs'
#modes = ['min', "low", "mid", "high"]
modes = ['min']
for folder in os.scandir(parent_directory):
    if folder.is_dir():
        # print(folder.name)
        for mode in modes:
            print("Currently running Fawkes with {} in {} mode".format(folder.name, mode))
            logFilePath = os.path.join(os.path.expanduser('~'), folder.name+'_'+ mode+'.log')
            bashCommand = "python3 ./fawkes/protection.py -d {} -m {} > {}".format(folder.name, mode, logFilePath)
            process = subprocess.run(bashCommand, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            print("Log file saved to {}".format(logFilePath))
