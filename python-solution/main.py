import os
import time
from FileNumberSummer import FileNumberSummer

# 1, 1000 because the files are named from 000001.csv to 001000.csv
start_time = time.time()
FNS = FileNumberSummer(os.getcwd() + "/files", 1, 1000)
print(FNS.getSum())
elapsed_time = time.time() - start_time
print("time: ", elapsed_time)