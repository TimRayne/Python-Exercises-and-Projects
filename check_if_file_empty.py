import os

check_file = os.stat("sample.txt").st_size

if(check_file == 0):
    print("The file is empty.")
else:
    print("The file is not empty.")