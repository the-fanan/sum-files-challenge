import os
from FileNumberSummer import FileNumberSummer
#os.chdir("../")
rootDir = os.getcwd()
filesDir = rootDir + "/files"

FNS = FileNumberSummer(filesDir)
print(FNS.getSum())
