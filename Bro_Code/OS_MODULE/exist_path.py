import os
#path = "C:\\Users\\yunee\\OneDrive\\Desktop\\test_python\\index.html"
path = "FILE\\test.txt"
if os.path.exists(path):
    print("this Path is exist")
    if os.path.isfile(path):
        print("this is a File")
    elif os.path.isdir(path):
        print("THis Direcory is avalibale")
else:
    print("this path is not exist")
