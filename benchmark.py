from subprocess import run

bashCommand = "python3 fawkes/protection.py -d {} -m {} > {}".format(dir, mode, logFilePath)

run(bashCommand)