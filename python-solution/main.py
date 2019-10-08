import os
from FileNumberSummer import FileNumberSummer

# 1, 1000 because the files are named from 000001.csv to 001000.csv
FNS = FileNumberSummer(os.getcwd() + "/files", 1, 1000)
print(FNS.getSum())

