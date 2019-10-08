import os
from FileNumberSummer import FileNumberSummer
os.chdir("../")
rootDir = os.getcwd() + "/files"
FNS = FileNumberSummer(rootDir, 1, 1000)
print(FNS.getSum())

